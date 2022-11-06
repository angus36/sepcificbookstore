import requests
url = "https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
res = response.json()
print(type(res))
import streamlit as st

def getAllBookstore():
     url = "https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M" # 在這裡輸入目標 url
     headers = {"accept": "application/json"}
     response = requests.get(url, headers=headers)
     res = response.json()
     return res


def getCountyOption(items):
    optionList = []
    for item in items:
        # 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
        name = item['cityName'][0:3]
        # hint: 想辦法處理 item['cityName'] 的內容

        # 如果 name 不在 optionList 之中，便把它放入 optionList
        if name not in optionList: optionList.append(name)
        # hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
    return optionList


def app():
    bookstoreList = getAllBookstore()
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList)) # 將 118 替換成書店的數量
    countyoption = getCountyOption(bookstoreList)
    county = st.selectbox('請選擇縣市', countyoption)

def getSpecificBookstore(items, county, districts):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        # 如果 name 不是我們選取的 county 則跳過
        if county not in name: continue 
        for district in districts:
    # hint: 用 if-else 判斷並用 continue 跳過

    # districts 是一個 list 結構，判斷 list 每個值是否出現在 name 之中
    # 判斷該項目是否已經出現在 specificBookstoreList 之中，沒有則放入
            if district not in name: continue
            specificBookstoreList.append(item)
    # hint: 用 for-loop 進行迭代，用 if-else 判斷，用 append 放入
    return specificBookstoreList

def getBookstoreInfo(items):
    expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        # 用 st.write 呈現書店的 Introduction
        expander.write(item['instro'])
        expander.subheader('Address')
        # 用 st.write 呈現書店的 Address
        expander.write(item['address'])
        expander.subheader('Open Time')
        # 用 st.write 呈現書店的 Open Time
        expander.write(item['openTime'])
        expander.subheader('Email') 
        # 用 st.write 呈現書店的 Email
        expander.write(item['email'])
        expanderList.append(expander)
        # 將該 expander 放到 expanderList 中
    return expanderList

def app():
	bookstoreList = getAllBookstore()
	countyOption = getCountyOption(bookstoreList)
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', countyOption) 
	districtOption = getDistrictOption(bookstoreList, county)
	district = st.multiselect('請選擇區域', districtOption) 
	specificBookstore = getSpecificBookstore(bookstoreList, county, district)
	num = len(specificBookstore)
	st.write(f'總共有{num}項結果', num)

if __name__ == "__main__":
    app()
