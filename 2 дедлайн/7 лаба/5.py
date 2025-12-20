def format_report(report_title: str, *data, **properties):
    print("=" * 50)
    print(f"отчет: {report_title}")
    print("=" * 50)
    if data:
        print("\nсодержание:")
        for i, item in enumerate(data, 1):
            print(f"  {i}. {item}")
    else:
        print("\nНет данных для отображения")
    if properties:
        print("\nметаданные:")
        for key, value in properties.items():
            print(f"  {key}: {value}")
    
    print("=" * 50)
    print("Конец отчета\n")