"""Сетевой IP сканер. Сканирует указанную сеть на наличие активных хостов"""

import ipaddress
import subprocess
import platform
import socket
import struct
import threading
import time
from queue import Queue
from datetime import datetime
import argparse
import sys
import os

class IPScanner:
    def __init__(self, network="192.168.1.0/24", timeout=1, max_threads=100):
        """Инициализация сканера
        
        Args:
            network (str): Сеть для сканирования в формате CIDR
            timeout (int): Таймаут для ping (секунды)
            max_threads (int): Максимальное количество потоков"""
        self.network = network
        self.timeout = timeout
        self.max_threads = max_threads
        self.active_hosts = []
        self.scan_queue = Queue()
        self.lock = threading.Lock()
        self.scan_progress = 0
        self.total_hosts = 0
        
    def validate_network(self):
        """Проверка корректности сетевого адреса"""
        try:
            network_obj = ipaddress.ip_network(self.network, strict=False)
            return network_obj
        except ValueError as e:
            print(f"Ошибка в формате сети: {e}")
            return None
    
    def ping_host(self, ip):
        """
        Проверка доступности хоста через ping
        
        Args:
            ip (str): IP адрес для проверки
            
        Returns:
            bool: True если хост отвечает на ping
        """
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', '-w', str(self.timeout * 1000), ip]
        
        try:
            # Для Linux/Mac добавляем флаг -W для таймаута
            if platform.system().lower() != 'windows':
                command = ['ping', '-c', '1', '-W', str(self.timeout), ip]
            
            result = subprocess.run(command, 
                                  stdout=subprocess.PIPE, 
                                  stderr=subprocess.PIPE,
                                  text=True)
            
            return result.returncode == 0
        except Exception:
            return False
    
    def scan_port(self, ip, port):
        """
        Проверка открытого порта на хосте
        
        Args:
            ip (str): IP адрес
            port (int): Порт для проверки
            
        Returns:
            bool: True если порт открыт
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except:
            return False
    
    def get_host_info(self, ip):
        """
        Получение информации о хосте
        
        Args:
            ip (str): IP адрес
            
        Returns:
            dict: Информация о хосте
        """
        info = {
            'ip': ip,
            'hostname': None,
            'mac_address': None,
            'open_ports': [],
            'os_type': None
        }
        
        # Получение hostname
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            info['hostname'] = hostname
        except (socket.herror, socket.gaierror):
            pass
        
        # Проверка основных портов
        common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389, 8080]
        for port in common_ports:
            if self.scan_port(ip, port):
                info['open_ports'].append(port)
        
        return info
    
    def worker_ping(self):
        """Рабочая функция для потоков ping"""
        while True:
            ip = self.scan_queue.get()
            if ip is None:
                break
            
            if self.ping_host(str(ip)):
                with self.lock:
                    self.active_hosts.append(str(ip))
                    print(f"Найден активный хост: {ip}")
            
            with self.lock:
                self.scan_progress += 1
            
            self.scan_queue.task_done()
    
    def scan_network(self):
        """
        Сканирование сети на активные хосты
        
        Returns:
            list: Список активных хостов
        """
        print(f"Начало сканирования сети: {self.network}")
        print(f"Таймаут: {self.timeout} сек, Потоков: {self.max_threads}")
        print("-" * 50)
        
        network_obj = self.validate_network()
        if not network_obj:
            return []
        
        # Создаем очередь IP адресов
        hosts = list(network_obj.hosts())
        self.total_hosts = len(hosts)
        
        if self.total_hosts == 0:
            print("Нет хостов для сканирования в указанной сети")
            return []
        
        print(f"Всего хостов для сканирования: {self.total_hosts}")
        
        # Заполняем очередь
        for host in hosts:
            self.scan_queue.put(host)
        
        # Создаем и запускаем потоки
        threads = []
        for _ in range(min(self.max_threads, self.total_hosts)):
            thread = threading.Thread(target=self.worker_ping)
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        # Ожидаем завершения очереди с прогрессом
        last_progress = 0
        while self.scan_progress < self.total_hosts:
            current_progress = self.scan_progress
            if current_progress > last_progress:
                percent = (current_progress / self.total_hosts) * 100
                print(f"Прогресс: {current_progress}/{self.total_hosts} ({percent:.1f}%)", end='\r')
                last_progress = current_progress
            time.sleep(0.1)
        
        # Останавливаем потоки
        for _ in range(len(threads)):
            self.scan_queue.put(None)
        
        for thread in threads:
            thread.join()
        
        print(f"\nСканирование завершено")
        print(f"Найдено активных хостов: {len(self.active_hosts)}")
        
        return self.active_hosts
    
    def detailed_scan(self, hosts=None):
        """
        Детальное сканирование найденных хостов
        
        Args:
            hosts (list): Список IP адресов для сканирования
            
        Returns:
            list: Детальная информация о хостах
        """
        if hosts is None:
            hosts = self.active_hosts
        
        if not hosts:
            print("[!] Нет хостов для детального сканирования")
            return []
        
        print(f"\n[*] Начало детального сканирования {len(hosts)} хостов")
        print("-" * 50)
        
        detailed_info = []
        for i, ip in enumerate(hosts, 1):
            print(f"[{i}/{len(hosts)}] Сканирую {ip}...")
            info = self.get_host_info(ip)
            detailed_info.append(info)
            
            # Вывод информации о хосте
            print(f"    IP: {info['ip']}")
            if info['hostname']:
                print(f"    Имя хоста: {info['hostname']}")
            if info['open_ports']:
                print(f"    Открытые порты: {', '.join(map(str, info['open_ports']))}")
            print()
        
        return detailed_info
    
    def save_results(self, detailed_info, filename=None):
        """
        Сохранение результатов сканирования в файл
        
        Args:
            detailed_info (list): Детальная информация о хостах
            filename (str): Имя файла для сохранения
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scan_results_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Результаты сканирования сети: {self.network}\n")
                f.write(f"Время сканирования: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Найдено хостов: {len(detailed_info)}\n")
                f.write("=" * 60 + "\n\n")
                
                for info in detailed_info:
                    f.write(f"IP адрес: {info['ip']}\n")
                    if info['hostname']:
                        f.write(f"Имя хоста: {info['hostname']}\n")
                    
                    if info['open_ports']:
                        f.write(f"Открытые порты: {', '.join(map(str, info['open_ports']))}\n")
                    else:
                        f.write("Открытые порты: не найдены\n")
                    
                    f.write("-" * 40 + "\n")
            
            print(f"Результаты сохранены в файл: {filename}")
            
        except Exception as e:
            print(f"Ошибка при сохранении результатов: {e}")

def print_banner():
    """Вывод баннера программы"""
    banner = """
    ╔═══════════════════════════════════════════════════════╗
    ║              СЕТЕВОЙ IP СКАНЕР                        ║
    ║             Автор: Лыков Арсений                      ║
    ╚═══════════════════════════════════════════════════════╝
    """
    print(banner)

def main():
    """Основная функция программы"""
    print_banner()
    
    parser = argparse.ArgumentParser(
        description='Сетевой IP сканер - обнаружение активных хостов в сети',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python ip_scanner.py                        # Сканирование сети по умолчанию
  python ip_scanner.py -n 192.168.0.0/24     # Сканирование указанной сети
  python ip_scanner.py -n 10.0.0.0/24 -t 50  # 50 потоков
  python ip_scanner.py -n 192.168.1.0/24 -o  # Только ping
  python ip_scanner.py --help                # Показать справку
        """
    )
    
    parser.add_argument('-n', '--network', 
                       default='192.168.1.0/24',
                       help='Сеть для сканирования в формате CIDR (по умолчанию: 192.168.1.0/24)')
    
    parser.add_argument('-t', '--threads', 
                       type=int, 
                       default=100,
                       help='Количество потоков (по умолчанию: 100)')
    
    parser.add_argument('-to', '--timeout', 
                       type=float, 
                       default=1.0,
                       help='Таймаут в секундах (по умолчанию: 1.0)')
    
    parser.add_argument('-o', '--only-ping', 
                       action='store_true',
                       help='Только ping-сканирование без детальной информации')
    
    parser.add_argument('-s', '--save', 
                       action='store_true',
                       help='Сохранить результаты в файл')
    
    parser.add_argument('-f', '--file',
                       help='Имя файла для сохранения результатов')
    
    args = parser.parse_args()
    
    try:
        # Создаем сканер
        scanner = IPScanner(
            network=args.network,
            timeout=args.timeout,
            max_threads=args.threads
        )
        
        # Сканируем сеть
        active_hosts = scanner.scan_network()
        
        if not active_hosts:
            print("Активные хосты не найдены")
            return
        
        # Детальное сканирование
        if not args.only_ping:
            detailed_info = scanner.detailed_scan(active_hosts)
            
            # Сохранение результатов
            if args.save or args.file:
                scanner.save_results(detailed_info, args.file)
        
        print("\nПрограмма завершена успешно")
        
    except KeyboardInterrupt:
        print("\n\nСканирование прервано пользователем")
        sys.exit(0)
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Проверка прав администратора/root (для raw socket операций)
    if platform.system().lower() != 'windows':
        if os.geteuid() != 0:
            print("Внимание: Для полного функционала запустите программу с правами root")
            print("Некоторые функции могут работать ограниченно")
            time.sleep(2)
    
    main()