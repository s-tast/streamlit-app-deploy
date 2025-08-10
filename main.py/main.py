def get_even_numbers(numbers):
    """
    リストから偶数だけを抽出する関数
    
    Args:
        numbers (list): 整数のリスト
    
    Returns:
        list: 偶数のみを含むリスト
    """
    return [num for num in numbers if num % 2 == 0]


def get_even_numbers_filter(numbers):
    """
    filter関数を使ってリストから偶数だけを抽出する関数
    
    Args:
        numbers (list): 整数のリスト
    
    Returns:
        list: 偶数のみを含むリスト
    """
    return list(filter(lambda x: x % 2 == 0, numbers))


def extract_even_numbers(numbers):
    """
    リストから偶数だけを抽出する関数
    
    Args:
        numbers (list): 整数のリスト
    
    Returns:
        list: 偶数のみを含むリスト
    """
    return [num for num in numbers if num % 2 == 0]


def categorize_numbers(numbers):
    """
    数値のリストを受け取り、各値に基づいてカテゴリを分類する関数
    
    Args:
        numbers (list): 整数のリスト
    
    Returns:
        dict: カテゴリ名をキー、該当する数値のリストを値とする辞書
              {"Low": [...], "Medium": [...], "High": [...]}
    """
    categories = {"Low": [], "Medium": [], "High": []}
    
    for num in numbers:
        if num <= 0:
            categories["Low"].append(num)
        elif 1 <= num <= 10:
            categories["Medium"].append(num)
        else:  # num > 10
            categories["High"].append(num)
    
    return categories


# テスト用のサンプルデータ
fruit_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":
    # 要素数が10のテストリストを作成
    test_list_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("元のリスト（要素数10）:", test_list_10)
    
    # extract_even_numbers関数を使って偶数を抽出
    even_numbers = extract_even_numbers(test_list_10)
    print("抽出された偶数:", even_numbers)
    
    # 戻り値のリストの合計値と平均値を計算
    if even_numbers:  # リストが空でない場合
        total_sum = sum(even_numbers)
        average = total_sum / len(even_numbers)
        
        print(f"偶数の合計値: {total_sum}")
        print(f"偶数の平均値: {average:.2f}")
        print(f"偶数の個数: {len(even_numbers)}")
    else:
        print("偶数が見つかりませんでした")
    
    print("-" * 40)
    
    # カテゴリ分類機能のテスト
    test_values = [-5, -1, 0, 1, 5, 10, 11, 15, 20, 25]
    print("カテゴリ分類のテスト")
    print("テスト用のリスト:", test_values)
    
    categories = categorize_numbers(test_values)
    print("分類結果:")
    for category, values in categories.items():
        print(f"  {category}: {values}")
    
    print("-" * 40)
    
    # 使用例（既存のコード）
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    print("元のリスト:", test_numbers)
    
    # リスト内包表記を使った方法
    even_nums1 = get_even_numbers(test_numbers)
    print("偶数（リスト内包表記）:", even_nums1)
    
    # filter関数を使った方法
    even_nums2 = get_even_numbers_filter(test_numbers)
    print("偶数（filter関数）:", even_nums2)
    
    # fruit_listからも偶数を抽出
    even_fruits = get_even_numbers(fruit_list)
    print("fruit_listの偶数:", even_fruits)
