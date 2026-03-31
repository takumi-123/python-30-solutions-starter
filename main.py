import requests
def main():   
 #データを受け取る
    url =  "https://jsonplaceholder.typicode.com/todos/1"
    #GETリクエストを送信してレスポンスを受け取る
    response = requests.get(url)

    #成功したかチェック
    if response.status_code == 200:
        #4 JSON データをpythonの辞書に変換
        data = response.json()
        #5 指定された形式で表示
        print(f"title:{data['title']}")

if __name__ == "__main__":
    main()