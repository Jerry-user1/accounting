import json
from pathlib import Path


DATA_FILE = Path("bills.json")


def load_bills():
    """从 JSON 文件加载账单数据"""
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("数据文件损坏，将使用空账单。")
        return []


def save_bills(bills):
    """保存账单数据到 JSON 文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            bills,
            file,
            ensure_ascii=False,
            indent=4
        )


def add_bill(bills):
    """添加一条账单"""
    try:
        amount = float(input("金额："))

        if amount < 0:
            print("金额不能为负数。")
            return

    except ValueError:
        print("金额必须是数字。")
        return

    category = input("类型：").strip()
    description = input("说明：").strip()
    date = input("日期（例如 2026-09-28）：").strip()

    bill = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    bills.append(bill)
    save_bills(bills)

    print("添加成功！")


def show_bills(bills):
    """显示所有账单"""
    if not bills:
        print("目前没有账单。")
        return

    print("\n" + "=" * 70)
    print(f"{'编号':<6}{'日期':<15}{'类型':<12}{'金额':<12}{'说明'}")
    print("=" * 70)

    for index, bill in enumerate(bills, start=1):
        print(
            f"{index:<6}"
            f"{bill['date']:<15}"
            f"{bill['category']:<12}"
            f"{bill['amount']:<12.2f}"
            f"{bill['description']}"
        )

    print("=" * 70)


def delete_bill(bills):
    """删除指定账单"""
    if not bills:
        print("目前没有账单。")
        return

    show_bills(bills)

    try:
        index = int(input("请输入要删除的账单编号："))

        if index < 1 or index > len(bills):
            print("编号不存在。")
            return

    except ValueError:
        print("请输入有效的数字编号。")
        return

    removed_bill = bills.pop(index - 1)
    save_bills(bills)

    print(
        f"已删除："
        f"{removed_bill['category']} "
        f"{removed_bill['amount']:.2f} 元"
    )


def update_bill(bills):
    """修改指定账单"""
    if not bills:
        print("目前没有账单。")
        return

    show_bills(bills)

    try:
        index = int(input("请输入要修改的账单编号："))

        if index < 1 or index > len(bills):
            print("编号不存在。")
            return

    except ValueError:
        print("请输入有效的数字编号。")
        return

    bill = bills[index - 1]

    print("\n直接回车表示保持原来的值。")

    amount_input = input(
        f"金额（当前：{bill['amount']}）："
    ).strip()

    if amount_input:
        try:
            amount = float(amount_input)

            if amount < 0:
                print("金额不能为负数。")
                return

            bill["amount"] = amount

        except ValueError:
            print("金额必须是数字。")
            return

    category = input(
        f"类型（当前：{bill['category']}）："
    ).strip()

    if category:
        bill["category"] = category

    description = input(
        f"说明（当前：{bill['description']}）："
    ).strip()

    if description:
        bill["description"] = description

    date = input(
        f"日期（当前：{bill['date']}）："
    ).strip()

    if date:
        bill["date"] = date

    save_bills(bills)

    print("修改成功！")


def search_by_category(bills):
    """按照类型查询账单"""
    if not bills:
        print("目前没有账单。")
        return

    category = input("请输入要查询的类型：").strip()

    results = []

    for bill in bills:
        if bill["category"] == category:
            results.append(bill)

    if not results:
        print(f"没有找到类型为「{category}」的账单。")
        return

    print(f"\n找到 {len(results)} 条账单：")

    print("\n" + "=" * 70)
    print(f"{'日期':<15}{'类型':<12}{'金额':<12}{'说明'}")
    print("=" * 70)

    for bill in results:
        print(
            f"{bill['date']:<15}"
            f"{bill['category']:<12}"
            f"{bill['amount']:<12.2f}"
            f"{bill['description']}"
        )

    print("=" * 70)


def show_statistics(bills):
    """显示账单统计信息"""
    if not bills:
        print("目前没有账单。")
        return

    total = 0

    category_totals = {}

    for bill in bills:
        amount = bill["amount"]
        category = bill["category"]

        total += amount

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    print("\n========== 账单统计 ==========")
    print(f"总支出：{total:.2f} 元")

    print("\n分类统计：")

    for category, amount in category_totals.items():
        print(f"{category}：{amount:.2f} 元")

    print("==============================")


def print_menu():
    """显示菜单"""
    print("\n" + "=" * 30)
    print("       个人记账系统")
    print("=" * 30)
    print("1. 添加账单")
    print("2. 查看账单")
    print("3. 删除账单")
    print("4. 修改账单")
    print("5. 按类型查询")
    print("6. 查看统计")
    print("0. 退出系统")
    print("=" * 30)


def main():
    """程序主函数"""
    bills = load_bills()

    while True:
        print_menu()

        choice = input("请选择：").strip()

        if choice == "1":
            add_bill(bills)

        elif choice == "2":
            show_bills(bills)

        elif choice == "3":
            delete_bill(bills)

        elif choice == "4":
            update_bill(bills)

        elif choice == "5":
            search_by_category(bills)

        elif choice == "6":
            show_statistics(bills)

        elif choice == "0":
            print("程序退出，再见！")
            break

        else:
            print("输入无效，请重新选择。")


if __name__ == "__main__":
    main()


"""
这是解决merge conflict 后的最终版本
"""

"""
dev分支测试
"""