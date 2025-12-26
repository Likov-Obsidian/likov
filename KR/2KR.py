def build_query(table, cols, **filters):
    select = f"SELECT {', '.join(cols)} FROM {table}"
    if filters:
        where = []
        for k, v in filters.items():
            val = f"'{v}'" if isinstance(v, str) else str(v)
            where.append(f"{k}={val}")
        return f"{select} WHERE {' AND '.join(where)};"
    return f"{select};"
query = build_query("users", ["имя", "email"], age=25, city="Нижневартовск")
print(query)