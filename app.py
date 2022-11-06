import requests
url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M'
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
#print(type(response))
res = response.json()
#print(type(res))
import streamlit as st

def app():
    bookstorelist = getAllBookstore()
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstorelist))
    countyOption = getCountyOption(bookstorelist)
    county = st.selectbox('請選擇縣市', countyOption)
    district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])

def getAllBookstore():
	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
	headers = {"accept": "application/json"}
	response =requests.get(url, headers=headers)
	res = response.json()# 將 response 轉換成 json 格式
	return res

def getCountyOption(items):
    optionList=[]
    # 創建一個空的 List 並命名為 optionList
    for item in items:
        name = item['cityName'][0:3]

        # 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
        # hint: 想辦法處理 item['cityName'] 的內容
        if name not in optionList:
            optionList.append(name)
        # 如果 name 不在 optionList 之中，便把它放入 optionList
        # hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
    return optionList

def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
     name = item['cityName']
     if name!=county : continue 
      # 如果 name 不是我們選取的 county 則跳過
      # hint: 用 if-else 判斷並用 continue 跳過
      for 
      # districts 是一個 list 結構，判斷 list 每個值是否出現在 name 之中
	  # 判斷該項目是否已經出現在 specificBookstoreList 之中，沒有則放入
	  # hint: 用 for-loop 進行迭代，用 if-else 判斷，用 append 放入
    return specificBookstoreList

def app():
	bookstoreList = getAllBookstore()

	countyOption = getCountyOption(bookstoreList)
	
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', countyOption) 
	 
	
	# 呼叫 getSpecificBookstore 並將回傳值賦值給變數 specificBookstore
	num = len(specificBookstore)
	# 用 st.write 將目標書店的總數量計算出來，格式：總共有3項結果

if __name__ == '__main__':
    app()
    # python -m streamlit run app.py




