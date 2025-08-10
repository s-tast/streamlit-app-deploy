def categorize_numbers(numbers):
    """
    数値のリストを受け取り、各値に基づいてカテゴリを分類する関数
    
    Args:
        numbers (list): 整数のリスト
    
    Returns:
        dict: カテゴリ名をキー、該当する数値のリストを値とする辞書
    """
    categories = {
        "Low": [],
        "Medium": [],
        "High": []
    }
    
    for num in numbers:
        if num <= 0:
            categories["Low"].append(num)
        elif 1 <= num <= 10:
            categories["Medium"].append(num)
        else:  # num > 10
            categories["High"].append(num)
    
    return categories


def calculate_bmi(weight, height):
    """
    BMI（Body Mass Index）を計算する関数
    
    Args:
        weight (float): 体重（kg）
        height (float): 身長（m）
    
    Returns:
        float: BMI値
    """
    if height <= 0:
        raise ValueError("身長は0より大きい値である必要があります")
    if weight <= 0:
        raise ValueError("体重は0より大きい値である必要があります")
    
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def categorize_bmi(bmi):
    """
    BMI値に基づいて体重カテゴリを分類する関数
    
    Args:
        bmi (float): BMI値
    
    Returns:
        str: 体重カテゴリ
    """
    if bmi < 18.5:
        return "低体重"
    elif 18.5 <= bmi < 25:
        return "普通体重"
    elif 25 <= bmi < 30:
        return "肥満（1度）"
    else:
        return "肥満（2度以上）"


def main():
    # 数値分類のテスト
    print("=== 数値分類テスト ===")
    test_numbers = [-5, 0, 1, 5, 10, 15, 20, -2, 3, 12]
    
    print("入力データ:", test_numbers)
    print()
    
    result = categorize_numbers(test_numbers)
    
    print("分類結果:")
    for category, values in result.items():
        print(f"{category}: {values}")
    
    print()
    print("各カテゴリの個数:")
    for category, values in result.items():
        print(f"{category}: {len(values)}個")
    
    print("\n" + "="*50 + "\n")
    
    # BMI計算のテスト
    print("=== BMI計算テスト ===")
    test_data = [
        (65, 1.70),  # 普通体重
        (50, 1.60),  # 低体重
        (80, 1.65),  # 肥満（1度）
        (90, 1.60),  # 肥満（2度以上）
    ]
    
    for weight, height in test_data:
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        print(f"体重: {weight}kg, 身長: {height}m → BMI: {bmi} ({category})")


if __name__ == "__main__":
    main()

