# ElementTree 모듈을 읽어온다
from xml.etree import ElementTree

# parse 함수로 파일을 읽어 들이고 ElementTree 객체를 만든다
tree = ElementTree.parse('rss.xml')

# getroot 메서드로 XML의 루트 요소를 추출한다
root = tree.getroot()

# findall 메서드로 요소 목록을 추출한다
for item in root.findall('channel/item/description/body/location/data'):
    # find 메서드로 요소를 찾고 text 속성으로 값을 출력한다
    tm_Ef = item.find('tmEf').text
    wf = item.find('wf').text
    tmn = item.find('tmn').text
    tmx = item.find('tmx').text
    print(tm_Ef, wf, tmn, tmx)
    