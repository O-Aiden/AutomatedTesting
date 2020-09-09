*** Settings ***
Library           TestLibrary
Library           RequestsLibrary

*** Keywords ***
DT_Hb_detector_post
    [Arguments]    ${url}    ${json}    ${User-Id}    ${Session-Id}
    [Documentation]   …    【功能】DemoPost … …    【参数】 …    url：请求域名 …    data：请求参数 …     …    【返回值】 …    Ret：response对象 
    ${headers}    Create Dictionary    User-Id=${User-Id} Session-Id=${Session-Id} Content-Type=application/json
    Create Session    api    ${url}    ${headers}   verify=${False}
    ${Ret}    Post Request   api   /detector/post    json=${json}
    [Return]    ${Ret}

DT_Hb_detector_post1
    [Arguments]    ${url}    ${json}    ${User-Id}    ${Session-Id}
    [Documentation]   …    【功能】DemoPost … …    【参数】 …    url：请求域名 …    data：请求参数 …     …    【返回值】 …    Ret：response对象 
    ${headers}    Create Dictionary    User-Id=${User-Id} Session-Id=${Session-Id} Content-Type=application/json
    Create Session    api    ${url}    ${headers}   verify=${False}
    ${Ret}    Post Request   api   /detector/post    json=${json}
    [Return]    ${Ret}

