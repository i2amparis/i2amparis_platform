from random import randint, choice, uniform  # Use it in function generate_data_for_heat_map

FAKE_DATA =[{"close_0": 296.0, "time": 1577743200000, "myVar1": 269.5, "open_0": 123.0},
 {"close_0": 155.0, "time": 1577829600000, "myVar1": 129.25, "open_0": 121.5},
 {"close_0": 182.5, "time": 1577916000000, "myVar1": 129.0, "open_0": 121.5},
 {"close_0": 162.5, "time": 1578002400000, "myVar1": 129.0, "open_0": 24.5},
 {"close_0": 127.5, "time": 1578088800000, "myVar1": 179.5, "open_0": 129.5},
 {"close_0": 124.0, "time": 1578175200000, "myVar1": 129.5, "open_0": 125.0},
 {"close_0": 229.5, "time": 1578261600000, "myVar1": 219.0, "open_0": 122.5},
 {"close_0": 228.0, "time": 1578348000000, "myVar1": 189.5, "open_0": 147.0},
 {"close_0": 288.0, "time": 1578434400000, "myVar1": 219.75, "open_0": 151.5},
 {"close_0": 337.5, "time": 1578520800000, "myVar1": 259.25, "open_0": 165.0},
 {"close_0": 349.5, "time": 1578607200000, "myVar1": 229.5, "open_0": 215.5},
 {"close_0": 342.0, "time": 1578693600000, "myVar1": 219.0, "open_0": 132.0},
 {"close_0": 552.5, "time": 1578780000000, "myVar1": 252.0, "open_0": 151.5},
 {"close_0": 300.0, "time": 1578866400000, "myVar1": 239.75, "open_0": 163.5},
 {"close_0": 421.0, "time": 1578952800000, "myVar1": 267.0, "open_0": 213.0},
 {"close_0": 436.0, "time": 1579039200000, "myVar1": 269.25, "open_0": 184.5},
 {"close_0": 464.0, "time": 1579125600000, "myVar1": 206.25, "open_0": 148.5},
 {"close_0": 258.0, "time": 1579212000000, "myVar1": 209.0, "open_0": 150.0},
 {"close_0": 307.0, "time": 1579298400000, "myVar1": 159.75, "open_0": 100.5},
 {"close_0": 190.5, "time": 1579384800000, "myVar1": 156.0, "open_0": 121.5},
 {"close_0": 205.5, "time": 1579471200000, "myVar1": 132.0, "open_0": 58.5},
 {"close_0": 190.5, "time": 1579557600000, "myVar1": 150.0, "open_0": 109.5},
 {"close_0": 231.0, "time": 1579644000000, "myVar1": 174.0, "open_0": 117.0},
 {"close_0": 190.5, "time": 1579730400000, "myVar1": 182.25, "open_0": 174.0},
 {"close_0": 197.0, "time": 1579816800000, "myVar1": 169.5, "open_0": 104.0},
 {"close_0": 411.5, "time": 1579903200000, "myVar1": 159.0, "open_0": 108.5},
 {"close_0": 419.5, "time": 1579989600000, "myVar1": 139.25, "open_0": 113.0},
 {"close_0": 261.5, "time": 1580076000000, "myVar1": 189.5, "open_0": 101.5},
 {"close_0": 408.0, "time": 1580162400000, "myVar1": 219.75, "open_0": 131.5},
 {"close_0": 540.5, "time": 1580248800000, "myVar1": 258.0, "open_0": 185.5},
 {"close_0": 341.0, "time": 1580335200000, "myVar1": 243.75, "open_0": 116.5},
 {"close_0": 307.0, "time": 1580421600000, "myVar1": 278.25, "open_0": 149.5},
 {"close_0": 311.5, "time": 1580508000000, "myVar1": 309.5, "open_0": 291.5},
 {"close_0": 345.0, "time": 1580594400000, "myVar1": 306.75, "open_0": 118.5},
{"close_1": 156.0, "time": 1577743200000, "myVar2": 169.5, "open_1": 183.0},
 {"close_1": 105.0, "time": 1577829600000, "myVar2": 143.25, "open_1": 181.5},
 {"close_1": 82.5, "time": 1577916000000, "myVar2": 117.0, "open_1": 151.5},
 {"close_1": 67.5, "time": 1578002400000, "myVar2": 111.0, "open_1": 154.5},
 {"close_1": 127.5, "time": 1578088800000, "myVar2": 178.5, "open_1": 229.5},
 {"close_1": 174.0, "time": 1578175200000, "myVar2": 199.5, "open_1": 225.0},
 {"close_1": 229.5, "time": 1578261600000, "myVar2": 216.0, "open_1": 202.5},
 {"close_1": 228.0, "time": 1578348000000, "myVar2": 187.5, "open_1": 147.0},
 {"close_1": 288.0, "time": 1578434400000, "myVar2": 219.75, "open_1": 151.5},
 {"close_1": 337.5, "time": 1578520800000, "myVar2": 251.25, "open_1": 165.0},
 {"close_1": 349.5, "time": 1578607200000, "myVar2": 292.5, "open_1": 235.5},
 {"close_1": 348.0, "time": 1578693600000, "myVar2": 270.0, "open_1": 192.0},
 {"close_1": 352.5, "time": 1578780000000, "myVar2": 252.0, "open_1": 151.5},
 {"close_1": 300.0, "time": 1578866400000, "myVar2": 231.75, "open_1": 163.5},
 {"close_1": 321.0, "time": 1578952800000, "myVar2": 267.0, "open_1": 213.0},
 {"close_1": 336.0, "time": 1579039200000, "myVar2": 260.25, "open_1": 184.5},
 {"close_1": 264.0, "time": 1579125600000, "myVar2": 206.25, "open_1": 148.5},
 {"close_1": 258.0, "time": 1579212000000, "myVar2": 204.0, "open_1": 150.0},
 {"close_1": 207.0, "time": 1579298400000, "myVar2": 153.75, "open_1": 100.5},
 {"close_1": 190.5, "time": 1579384800000, "myVar2": 156.0, "open_1": 121.5},
 {"close_1": 205.5, "time": 1579471200000, "myVar2": 132.0, "open_1": 58.5},
 {"close_1": 190.5, "time": 1579557600000, "myVar2": 150.0, "open_1": 109.5},
 {"close_1": 231.0, "time": 1579644000000, "myVar2": 174.0, "open_1": 117.0},
 {"close_1": 190.5, "time": 1579730400000, "myVar2": 182.25, "open_1": 174.0},
 {"close_1": 117.0, "time": 1579816800000, "myVar2": 160.5, "open_1": 204.0},
 {"close_1": 91.5, "time": 1579903200000, "myVar2": 150.0, "open_1": 208.5},
 {"close_1": 19.5, "time": 1579989600000, "myVar2": 131.25, "open_1": 243.0},
 {"close_1": 61.5, "time": 1580076000000, "myVar2": 181.5, "open_1": 301.5},
 {"close_1": 108.0, "time": 1580162400000, "myVar2": 219.75, "open_1": 331.5},
 {"close_1": 130.5, "time": 1580248800000, "myVar2": 258.0, "open_1": 385.5},
 {"close_1": 171.0, "time": 1580335200000, "myVar2": 243.75, "open_1": 316.5},
 {"close_1": 207.0, "time": 1580421600000, "myVar2": 278.25, "open_1": 349.5},
 {"close_1": 211.5, "time": 1580508000000, "myVar2": 301.5, "open_1": 391.5},
 {"close_1": 195.0, "time": 1580594400000, "myVar2": 306.75, "open_1": 418.5}
]


COLUMNCHART_DATA = [{
 "country": "USA",
 "year2017": 3.5,
 "year2018": 4.2
}, {
 "country": "UK",
 "year2017": 1.7,
 "year2018": 3.1
}, {
 "country": "Canada",
 "year2017": 2.8,
 "year2018": 2.9
}, {
 "country": "Japan",
 "year2017": 2.6,
 "year2018": 2.3
}, {
 "country": "France",
 "year2017": 1.4,
 "year2018": 2.1
}, {
 "country": "Brazil",
 "year2017": 2.6,
 "year2018": 4.9
}, {
 "country": "Russia",
 "year2017": 6.4,
 "year2018": 7.2
}, {
 "country": "India",
 "year2017": 8,
 "year2018": 7.1
}, {
 "country": "China",
 "year2017": 9.9,
 "year2018": 10.1
}]

BAR_RANGE_CHART_DATA = [
 {
  "name": "John",
  "fromDate": "2018-01-01 08:00",
  "toDate": "2018-01-01 10:00",
 },
 {
  "name": "John",
  "fromDate": "2018-01-01 12:00",
  "toDate": "2018-01-01 15:00",
 },
 {
  "name": "John",
  "fromDate": "2018-01-01 15:30",
  "toDate": "2018-01-01 21:30",
 },

 {
  "name": "Jane",
  "fromDate": "2018-01-01 09:00",
  "toDate": "2018-01-01 12:00",
 },
 {
  "name": "Jane",
  "fromDate": "2018-01-01 13:00",
  "toDate": "2018-01-01 17:00",
 },

 {
  "name": "Peter",
  "fromDate": "2018-01-01 11:00",
  "toDate": "2018-01-01 16:00",
 },
 {
  "name": "Peter",
  "fromDate": "2018-01-01 16:00",
  "toDate": "2018-01-01 19:00",
 },

 {
  "name": "Melania",
  "fromDate": "2018-01-01 16:00",
  "toDate": "2018-01-01 20:00",
 },
 {
  "name": "Melania",
  "fromDate": "2018-01-01 20:30",
  "toDate": "2018-01-01 24:00",
 },

 {
  "name": "Donald",
  "fromDate": "2018-01-01 13:00",
  "toDate": "2018-01-01 24:00",
 }
]
BAR_RANGE_CHART_DATA_2 = [
 {
  "region": "MENA",
  "name": "TIAM",
  "from": 5,
  "to": 10,
 },
 {
  "region":"Russia",
  "name": "GCAM",
  "from": 11,
  "to": 25,
 },
 {
  "region":"Latin America",
  "name": "42",
  "from": 10,
  "to": 20,
 },

 {
  "region":"India",
  "name": "ALADIN",
  "from": 20,
  "to": 25,
 },
 {
  "region":"Rest of Asia",
  "name": "ICES",
  "from": 25,
  "to": 30,
 },

 {
  "region":"Africa",
  "name": "NATEM",
  "from": 30,
  "to": 35,
 },
 {
  "region":"China",
  "name": "MAPLE",
  "from": 15,
  "to": 40,
 },

 {
  "region":"Europe",
  "name": "CONTO",
  "from": 40,
  "to": 45,
 },
 {
  "region":"Pacific OECD",
  "name": "NEMESIS",
  "from": 35,
  "to": 50,
 },

 {
  "region":"North America",
  "name": "LEAP",
  "from": 40,
  "to": 55,
 },
{
  "region":"World",
  "name": "FORECAST",
  "from": 50,
  "to": 60,
 }
]

BAR_HEATMAP_DATA = [{
 "category": "Research",
 "value": 450
}, {
 "category": "Marketing",
 "value": 1200
}, {
 "category": "Distribution",
 "value": 1850
}, {
 "category": "HR",
 "value": 850
}, {
 "category": "Sales",
 "value": 499
}, {
 "category": "Support",
 "value": 871
}, {
 "category": "Other",
 "value": 512
}]

BAR_HEATMAP_DATA_2 = [{
 "category": "GCAM",
 "precision": 45
}, {
 "category": "TIAM",
 "precision": 12
}, {
 "category": "MUSE",
 "precision": 18.5
}, {
 "category": "42",
 "precision": 8.5
}, {
 "category": "GEMINI-E3",
 "precision": 49.9
}, {
 "category": "ICES",
 "precision": 8.7
}, {
 "category": "DICE",
 "precision": 51.2
},
    {
 "category": "E3ME",
 "precision": 5.1
},
{
 "category": "ALADIN",
 "precision": 12
},
{
 "category": "FORECAST",
 "precision": 20
},
{
 "category": "LEAP",
 "precision": 33
},
{
 "category": "EU-TIMES",
 "precision": 42
},
{
 "category": "NEMESIS",
 "precision": 62
},
{
 "category": "CONTO",
 "precision": 27
},
{
 "category": "MARKAL-India",
 "precision": 51
},
{
 "category": "MAPLE",
 "precision": 24
},
{
 "category": "NATEM",
 "precision": 77
},
{
 "category": "SISGEMA",
 "precision": 88
},
{
 "category": "TIMES-CAC",
 "precision": 33
},
]
MORE_MAP_HEATMAP_DATA = [
    {
        "id": "AR",
        "value": 11
    },
    {
        "id": "AU",
        "value": 12
    },
    {
        "id": "BR",
        "value": 23
    },
    {
        "id": "CA",
        "value": 19
    },
    {
        "id": "CN",
        "value": 43
    },
    {
        "id": "FR",
        "value": 46
    },
    {
        "id": "GB",
        "value": 46
    },
    {
        "id": "IE",
        "value": 46
    },
    {
        "id": "ES",
        "value": 46
    },
    {
        "id": "PT",
        "value": 46
    },
    {
        "id": "IT",
        "value": 46
    },
    {
        "id": "DE",
        "value": 46
    },
    {
        "id": "GR",
        "value": 46
    },
    {
        "id": "CS",
        "value": 46
    },
    {
        "id": "HR",
        "value": 46
    },
    {
        "id": "AT",
        "value": 46
    },
    {
        "id": "FI",
        "value": 46
    },
    {
        "id": "SE",
        "value": 46
    },
    {
        "id": "PL",
        "value": 46
    },
    {
        "id": "BE",
        "value": 46
    },
    {
        "id": "BG",
        "value": 46
    },
    {
        "id": "CY",
        "value": 46
    },
    {
        "id": "CZ",
        "value": 46
    },
    {
        "id": "EE",
        "value": 46
    },
    {
        "id": "HU",
        "value": 46
    },
    {
        "id": "LV",
        "value": 46
    },
    {
        "id": "LT",
        "value": 46
    },
    {
        "id": "MT",
        "value": 46
    },
    {
        "id": "NL",
        "value": 46
    },
    {
        "id": "RO",
        "value": 46
    },
    {
        "id": "SK",
        "value": 46
    },
    {
        "id": "IN",
        "value": 36
    },
    {
        "id": "ID",
        "value": 11
    },
    {
        "id": "JP",
        "value": 16
    },
    {
        "id": "MX",
        "value": 10
    },
    {
        "id": "KR",
        "value": 17
    },
    {
        "id": "RU",
        "value": 25
    },
    {
        "id": "SA",
        "value": 3
    },
    {
        "id": "ZA",
        "value": 8
    },
    {
        "id": "TR",
        "value": 10
    },
    {
        "id": "US",
        "value": 40
    },
    {
        "id": "NG",
        "value": 1
    },
    {
        "id": "ET",
        "value": 1
    },
    {
        "id": "EG",
        "value": 1
    },
    {
        "id": "CD",
        "value": 1
    },
    {
        "id": "TZ",
        "value": 1
    },
    {
        "id": "KE",
        "value": 1
    },
    {
        "id": "UG",
        "value": 1
    },
    {
        "id": "DZ",
        "value": 1
    },
    {
        "id": "SD",
        "value": 1
    },
    {
        "id": "MA",
        "value": 1
    },
    {
        "id": "MZ",
        "value": 1
    },
    {
        "id": "GH",
        "value": 1
    },
    {
        "id": "AO",
        "value": 1
    },
    {
        "id": "SO",
        "value": 1
    },
    {
        "id": "CI",
        "value": 1
    },
    {
        "id": "MG",
        "value": 1
    },
    {
        "id": "CM",
        "value": 1
    },
    {
        "id": "BF",
        "value": 1
    },
    {
        "id": "NE",
        "value": 1
    },
    {
        "id": "MW",
        "value": 1
    },
    {
        "id": "ZM",
        "value": 1
    },
    {
        "id": "ML",
        "value": 1
    },
    {
        "id": "SN",
        "value": 1
    },
    {
        "id": "ZW",
        "value": 1
    },
    {
        "id": "TD",
        "value": 1
    },
    {
        "id": "TN",
        "value": 1
    },
    {
        "id": "GN",
        "value": 1
    },
    {
        "id": "RW",
        "value": 1
    },
    {
        "id": "BJ",
        "value": 1
    },
    {
        "id": "BI",
        "value": 1
    },
    {
        "id": "SS",
        "value": 1
    },
    {
        "id": "ER",
        "value": 1
    },
    {
        "id": "SL",
        "value": 1
    },
    {
        "id": "TG",
        "value": 1
    },
    {
        "id": "LY",
        "value": 1
    },
    {
        "id": "CF",
        "value": 1
    },
    {
        "id": "MR",
        "value": 1
    },
    {
        "id": "CG",
        "value": 1
    },
    {
        "id": "LR",
        "value": 1
    },
    {
        "id": "NA",
        "value": 1
    },
    {
        "id": "BW",
        "value": 1
    },
    {
        "id": "LS",
        "value": 1
    },
    {
        "id": "GM",
        "value": 1
    },
    {
        "id": "GA",
        "value": 1
    },
    {
        "id": "GW",
        "value": 1
    },
    {
        "id": "MU",
        "value": 1
    },
    {
        "id": "GQ",
        "value": 1
    },
    {
        "id": "",
        "value": 1
    },
    {
        "id": "DJ",
        "value": 1
    },
    {
        "id": "RE",
        "value": 1
    },
    {
        "id": "KM",
        "value": 1
    },
    {
        "id": "EH",
        "value": 1
    },
    {
        "id": "CV",
        "value": 1
    },
    {
        "id": "YT",
        "value": 1
    },
    {
        "id": "ST",
        "value": 1
    },
    {
        "id": "SC",
        "value": 1
    },
    {
        "id": "SH",
        "value": 1
    },
    {
        "id": "CO",
        "value": 1
    },
    {
        "id": "PE",
        "value": 1
    },
    {
        "id": "VE",
        "value": 1
    },
    {
        "id": "CL",
        "value": 1
    },
    {
        "id": "EC",
        "value": 1
    },
    {
        "id": "BO",
        "value": 1
    },
    {
        "id": "PY",
        "value": 1
    },
    {
        "id": "UY",
        "value": 1
    },
    {
        "id": "GY",
        "value": 1
    },
    {
        "id": "SR",
        "value": 1
    },
    {
        "id": "GF",
        "value": 1
    },
    {
        "id": "FK",
        "value": 1
    },
    {
        "id": "UA",
        "value": 1
    },
    {
        "id": "BY",
        "value": 1
    },
    {
        "id": "KZ",
        "value": 1
    },
    {
        "id": "UZ",
        "value": 1
    },
    {
        "id": "TM",
        "value": 1
    },
    {
        "id": "MN",
        "value": 1
    },
    {
        "id": "KH",
        "value": 1
    },
    {
        "id": "PH",
        "value": 1
    },
    {
        "id": "NO",
        "value": 1
    },
    {
        "id": "CH",
        "value": 1
    },
    {
        "id": "AL",
        "value": 1
    },
    {
        "id": "AM",
        "value": 1
    },
    {
        "id": "AZ",
        "value": 1
    },
    {
        "id": "BD",
        "value": 1
    },
    {
        "id": "BA",
        "value": 1
    },
    {
        "id": "CL",
        "value": 1
    },
    {
        "id": "CO",
        "value": 1
    },
    {
        "id": "CR",
        "value": 1
    },
    {
        "id": "CU",
        "value": 1
    },
    {
        "id": "SV",
        "value": 1
    },
    {
        "id": "GE",
        "value": 1
    },
    {
        "id": "GT",
        "value": 1
    },
    {
        "id": "HT",
        "value": 1
    },
    {
        "id": "HN",
        "value": 1
    },
    {
        "id": "IS",
        "value": 1
    },
    {
        "id": "IR",
        "value": 1
    },
    {
        "id": "IQ",
        "value": 1
    },
    {
        "id": "IL",
        "value": 1
    },
    {
        "id": "JM",
        "value": 1
    },
    {
        "id": "JO",
        "value": 1
    },
    {
        "id": "XK",
        "value": 1
    },
    {
        "id": "KW",
        "value": 1
    },
    {
        "id": "KG",
        "value": 1
    },
    {
        "id": "LA",
        "value": 1
    },
    {
        "id": "LB",
        "value": 1
    },
    {
        "id": "MK",
        "value": 1
    },
    {
        "id": "MY",
        "value": 1
    },
    {
        "id": "MD",
        "value": 1
    },
    {
        "id": "ME",
        "value": 1
    },
    {
        "id": "MM",
        "value": 1
    },
    {
        "id": "NP",
        "value": 1
    },
    {
        "id": "NZ",
        "value": 1
    },
    {
        "id": "NI",
        "value": 1
    },
    {
        "id": "KP",
        "value": 1
    },
    {
        "id": "OM",
        "value": 1
    },
    {
        "id": "PK",
        "value": 1
    },
    {
        "id": "PA",
        "value": 1
    },
    {
        "id": "QA",
        "value": 1
    },
    {
        "id": "SG",
        "value": 1
    },
    {
        "id": "",
        "value": 1
    },
    {
        "id": "SY",
        "value": 1
    },
    {
        "id": "TJ",
        "value": 1
    },
    {
        "id": "TH",
        "value": 1
    },
    {
        "id": "AE",
        "value": 1
    },
    {
        "id": "VN",
        "value": 1
    },
    {
        "id": "YE",
        "value": 1
    },

]

HEAT_MAP_DATA_FOR_MAP = [{"id": "US", "value": 18}, {"id": "MF", "value": 15}, {"id": "NU", "value": 16},
                         {"id": "BF", "value": 18}, {"id": "TF", "value": 13}, {"id": "GU", "value": 16},
                         {"id": "NC", "value": 17}, {"id": "TV", "value": 16}, {"id": "CC", "value": 16},
                         {"id": "MS", "value": 17}, {"id": "UA", "value": 20}, {"id": "CK", "value": 17},
                         {"id": "GB", "value": 24}, {"id": "HM", "value": 13}, {"id": "NZ", "value": 17},
                         {"id": "CX", "value": 15}, {"id": "KY", "value": 17}, {"id": "RU", "value": 18},
                         {"id": "VG", "value": 16}, {"id": "BB", "value": 18}, {"id": "NF", "value": 16},
                         {"id": "CF", "value": 18}, {"id": "GL", "value": 15}, {"id": "VC", "value": 18},
                         {"id": "AE", "value": 18}, {"id": "FK", "value": 16}, {"id": "LY", "value": 18},
                         {"id": "WF", "value": 14}, {"id": "AQ", "value": 13}, {"id": "SJ", "value": 14},
                         {"id": "GP", "value": 16}, {"id": "AG", "value": 17}, {"id": "TK", "value": 16},
                         {"id": "SB", "value": 17}, {"id": "GF", "value": 16}, {"id": "TW", "value": 17},
                         {"id": "SX", "value": 15}, {"id": "EH", "value": 17}, {"id": "PN", "value": 16},
                         {"id": "GE", "value": 19}, {"id": "VA", "value": 14}, {"id": "IE", "value": 27},
                         {"id": "SY", "value": 18}, {"id": "LC", "value": 18}, {"id": "GD", "value": 18},
                         {"id": "RE", "value": 16}, {"id": "AX", "value": 13}, {"id": "CA", "value": 18},
                         {"id": "TM", "value": 18}, {"id": "BM", "value": 18}, {"id": "YE", "value": 18},
                         {"id": "MN", "value": 17}, {"id": "BL", "value": 15}, {"id": "IM", "value": 13},
                         {"id": "PM", "value": 15}, {"id": "JP", "value": 18}, {"id": "CW", "value": 15},
                         {"id": "PF", "value": 16}, {"id": "AI", "value": 17}, {"id": "SH", "value": 16},
                         {"id": "BZ", "value": 17}, {"id": "CZ", "value": 26}, {"id": "BV", "value": 13},
                         {"id": "AS", "value": 16}, {"id": "RO", "value": 28}, {"id": "LA", "value": 17},
                         {"id": "FO", "value": 13}, {"id": "SS", "value": 18}, {"id": "TC", "value": 16},
                         {"id": "BN", "value": 17}, {"id": "AN", "value": 18}, {"id": "MY", "value": 17},
                         {"id": "BA", "value": 21}, {"id": "VI", "value": 16}, {"id": "DO", "value": 18},
                         {"id": "AW", "value": 17}, {"id": "GS", "value": 13}, {"id": "GI", "value": 15},
                         {"id": "IO", "value": 14}, {"id": "SK", "value": 25}, {"id": "JM", "value": 18},
                         {"id": "MQ", "value": 16}, {"id": "YT", "value": 16}, {"id": "KG", "value": 18},
                         {"id": "UM", "value": 16}, {"id": "BI", "value": 18}, {"id": "ZA", "value": 19},
                         {"id": "TN", "value": 18}, {"id": "JO", "value": 18}, {"id": "TZ", "value": 18},
                         {"id": "NO", "value": 26}, {"id": "GG", "value": 13}, {"id": "ZW", "value": 18},
                         {"id": "AO", "value": 18}, {"id": "KM", "value": 17}, {"id": "MG", "value": 18},
                         {"id": "ES", "value": 29}, {"id": "ET", "value": 18}, {"id": "LI", "value": 14},
                         {"id": "FJ", "value": 17}, {"id": "CM", "value": 18}, {"id": "TD", "value": 18},
                         {"id": "SC", "value": 17}, {"id": "CH", "value": 22}, {"id": "CU", "value": 18},
                         {"id": "MT", "value": 20}, {"id": "MV", "value": 17}, {"id": "PG", "value": 17},
                         {"id": "HK", "value": 16}, {"id": "MO", "value": 16}, {"id": "RS", "value": 23},
                         {"id": "LR", "value": 18}, {"id": "PA", "value": 18}, {"id": "PH", "value": 17},
                         {"id": "SA", "value": 17}, {"id": "GA", "value": 18}, {"id": "RW", "value": 18},
                         {"id": "MP", "value": 16}, {"id": "AR", "value": 17}, {"id": "ST", "value": 18},
                         {"id": "CV", "value": 18}, {"id": "FR", "value": 30}, {"id": "IR", "value": 17},
                         {"id": "KI", "value": 17}, {"id": "SM", "value": 14}, {"id": "PR", "value": 16},
                         {"id": "CR", "value": 18}, {"id": "BR", "value": 20}, {"id": "MZ", "value": 18},
                         {"id": "BW", "value": 18}, {"id": "OM", "value": 18}, {"id": "CN", "value": 18},
                         {"id": "GN", "value": 18}, {"id": "ZM", "value": 18}, {"id": "ER", "value": 18},
                         {"id": "ID", "value": 18}, {"id": "SE", "value": 26}, {"id": "MH", "value": 16},
                         {"id": "MD", "value": 20}, {"id": "BD", "value": 17}, {"id": "TT", "value": 18},
                         {"id": "NR", "value": 16}, {"id": "CO", "value": 18}, {"id": "MR", "value": 18},
                         {"id": "PT", "value": 25}, {"id": "AT", "value": 26}, {"id": "GW", "value": 18},
                         {"id": "IL", "value": 18}, {"id": "QA", "value": 18}, {"id": "SZ", "value": 18},
                         {"id": "VU", "value": 17}, {"id": "SN", "value": 18}, {"id": "BO", "value": 18},
                         {"id": "PW", "value": 16}, {"id": "CL", "value": 17}, {"id": "HU", "value": 26},
                         {"id": "NI", "value": 18}, {"id": "BT", "value": 17}, {"id": "GY", "value": 18},
                         {"id": "SL", "value": 18}, {"id": "EE", "value": 23}, {"id": "IT", "value": 29},
                         {"id": "BJ", "value": 18}, {"id": "CI", "value": 18}, {"id": "ML", "value": 18},
                         {"id": "TG", "value": 18}, {"id": "CY", "value": 20}, {"id": "KN", "value": 17},
                         {"id": "LU", "value": 25}, {"id": "BY", "value": 19}, {"id": "SI", "value": 24},
                         {"id": "HN", "value": 18}, {"id": "MC", "value": 15}, {"id": "BS", "value": 18},
                         {"id": "IS", "value": 19}, {"id": "BG", "value": 23}, {"id": "TR", "value": 18},
                         {"id": "MX", "value": 18}, {"id": "JE", "value": 13}, {"id": "HT", "value": 18},
                         {"id": "CD", "value": 18}, {"id": "CG", "value": 18}, {"id": "ME", "value": 22},
                         {"id": "VN", "value": 17}, {"id": "DM", "value": 18}, {"id": "NA", "value": 18},
                         {"id": "MA", "value": 18}, {"id": "AU", "value": 17}, {"id": "PY", "value": 18},
                         {"id": "KW", "value": 18}, {"id": "SR", "value": 18}, {"id": "BE", "value": 26},
                         {"id": "KR", "value": 15}, {"id": "GT", "value": 18}, {"id": "VE", "value": 18},
                         {"id": "DJ", "value": 18}, {"id": "EC", "value": 18}, {"id": "TH", "value": 17},
                         {"id": "IQ", "value": 18}, {"id": "LT", "value": 25}, {"id": "MK", "value": 22},
                         {"id": "GM", "value": 18}, {"id": "PS", "value": 17}, {"id": "LB", "value": 18},
                         {"id": "TL", "value": 16}, {"id": "TJ", "value": 18}, {"id": "SV", "value": 18},
                         {"id": "EG", "value": 18}, {"id": "NG", "value": 18}, {"id": "KZ", "value": 18},
                         {"id": "DZ", "value": 18}, {"id": "PL", "value": 25}, {"id": "GR", "value": 29},
                         {"id": "HR", "value": 24}, {"id": "PE", "value": 18}, {"id": "WS", "value": 17},
                         {"id": "AM", "value": 19}, {"id": "PK", "value": 16}, {"id": "AZ", "value": 19},
                         {"id": "LV", "value": 28}, {"id": "TO", "value": 17}, {"id": "UY", "value": 18},
                         {"id": "FI", "value": 25}, {"id": "SD", "value": 18}, {"id": "AD", "value": 15},
                         {"id": "MM", "value": 17}, {"id": "LS", "value": 18}, {"id": "DE", "value": 30},
                         {"id": "NP", "value": 17}, {"id": "KH", "value": 17}, {"id": "KE", "value": 18},
                         {"id": "NE", "value": 18}, {"id": "AF", "value": 17}, {"id": "DK", "value": 26},
                         {"id": "BH", "value": 18}, {"id": "IN", "value": 18}, {"id": "BQ", "value": 15},
                         {"id": "MW", "value": 18}, {"id": "GH", "value": 18}, {"id": "UZ", "value": 18},
                         {"id": "SG", "value": 17}, {"id": "NL", "value": 26}, {"id": "MU", "value": 18},
                         {"id": "GQ", "value": 18}, {"id": "LK", "value": 17}, {"id": "FM", "value": 16},
                         {"id": "SO", "value": 18}, {"id": "AL", "value": 22}, {"id": "UG", "value": 18},
                         {"id": "KP", "value": 17}, {"id": "XK", "value": 13}, {"id": "XX", "value": 13}]

HEAT_MAP_DATA = [
    {
        "id": "AR",
        "value": 11
    },
    {
        "id": "AU",
        "value": 12
    },
    {
        "id": "BR",
        "value": 23
    },
    {
        "id": "CA",
        "value": 19
    },
    {
        "id": "CN",
        "value": 43
    },
    {
        "id": "FR",
        "value": 46
    },
    {
        "id": "GB",
        "value": 46
    },
    {
        "id": "IE",
        "value": 46
    },
    {
        "id": "ES",
        "value": 46
    },
    {
        "id": "PT",
        "value": 46
    },
    {
        "id": "IT",
        "value": 46
    },
    {
        "id": "DE",
        "value": 46
    },
    {
        "id": "GR",
        "value": 46
    },
    {
        "id": "CS",
        "value": 46
    },
    {
        "id": "HR",
        "value": 46
    },
    {
        "id": "AT",
        "value": 46
    },
    {
        "id": "FI",
        "value": 46
    },
    {
        "id": "SE",
        "value": 46
    },
    {
        "id": "PL",
        "value": 46
    },
    {
        "id": "BE",
        "value": 46
    },
    {
        "id": "BG",
        "value": 46
    },
    {
        "id": "CY",
        "value": 46
    },
    {
        "id": "CZ",
        "value": 46
    },
    {
        "id": "EE",
        "value": 46
    },
    {
        "id": "HU",
        "value": 46
    },
    {
        "id": "LV",
        "value": 46
    },
    {
        "id": "LT",
        "value": 46
    },
    {
        "id": "MT",
        "value": 46
    },
    {
        "id": "NL",
        "value": 46
    },
    {
        "id": "RO",
        "value": 46
    },
    {
        "id": "SK",
        "value": 46
    },
    {
        "id": "IN",
        "value": 36
    },
    {
        "id": "ID",
        "value": 11
    },
    {
        "id": "JP",
        "value": 16
    },
    {
        "id": "MX",
        "value": 10
    },
    {
        "id": "KR",
        "value": 17
    },
    {
        "id": "RU",
        "value": 25
    },
    {
        "id": "SA",
        "value": 3
    },
    {
        "id": "ZA",
        "value": 8
    },
    {
        "id": "TR",
        "value": 10
    },
    {
        "id": "US",
        "value": 40
    },

]

PIE_CHART_DATA = [
    {
        "country": "Lithuania",
        "oil_consumption": 501.9
    },
    {
        "country": "Czech Republic",
        "oil_consumption": 301.9
    },
    {
        "country": "Ireland",
        "oil_consumption": 201.1
    },
    {
        "country": "Germany",
        "oil_consumption": 165.8
    },
    {
        "country": "Australia",
        "oil_consumption": 139.9
    },
    {
        "country": "Austria",
        "oil_consumption": 128.3
    },
    {
        "country": "UK",
        "oil_consumption": 99
    },
    {
        "country": "Belgium",
        "oil_consumption": 60
    },
    {
        "country": "The Netherlands",
        "oil_consumption": 50
    }
]

RADAR_CHART_DATA = [
    {
        "country": "Lithuania",
        "oil_consumption": 501.9,
        "energy_consumption": 700
    },
    {
        "country": "Czech Republic",
        "oil_consumption": 301.9,
        "energy_consumption": 900
    },
    {
        "country": "Ireland",
        "oil_consumption": 201.1,
        "energy_consumption": 750
    },
    {
        "country": "Germany",
        "oil_consumption": 165.8,
        "energy_consumption": 300
    },
    {
        "country": "Australia",
        "oil_consumption": 139.9,
        "energy_consumption": 200
    },
    {
        "country": "Austria",
        "oil_consumption": 128.3,
        "energy_consumption": 500
    },
    {
        "country": "UK",
        "oil_consumption": 99,
        "energy_consumption": 700
    },
    {
        "country": "Belgium",
        "oil_consumption": 60,
        "energy_consumption": 200
    },
    {
        "country": "The Netherlands",
        "oil_consumption": 50,
        "energy_consumption": 700
    }
]

SANKEYCHORD_DATA = [
    {"from": "A", "to": "D", "value": 10},
    {"from": "B", "to": "D", "value": 8},
    {"from": "B", "to": "E", "value": 4},
    {"from": "C", "to": "E", "value": 3},
    {"from": "D", "to": "G", "value": 5},
    {"from": "D", "to": "I", "value": 2},
    {"from": "D", "to": "H", "value": 3},
    {"from": "E", "to": "H", "value": 6},
    {"from": "G", "to": "J", "value": 5},
    {"from": "I", "to": "J", "value": 1},
    {"from": "H", "to": "J", "value": 9}
]

SANKEYCHORD_DATA_3=[
    {"from": "Data Collection", "to": "Prevention & Preparedness", "value": 30},
    {"from": "Data Collection", "to": "Detection & Response", "value": 30},
    {"from": "Data Collection", "to": "Restoration & Adaptation", "value": 30},
    {"from": "Decision Support Systems", "to": "Prevention & Preparedness", "value": 30},
    {"from": "Decision Support Systems", "to": "Detection & Response", "value": 30},
    {"from": "Decision Support Systems", "to": "Restoration & Adaptation", "value": 30},
    {"from": "Emergency Communication", "to": "Prevention & Preparedness", "value": 10},
    {"from": "Emergency Communication", "to": "Detection & Response", "value": 30},
    {"from": "Emergency Communication", "to": "Restoration & Adaptation", "value": 10},
    {"from": "Long-term Impact on Climate Change", "to": "Prevention & Preparedness", "value": 30},
    {"from": "Long-term Impact on Climate Change", "to": "Detection & Response", "value": 20},
    {"from": "Long-term Impact on Climate Change", "to": "Restoration & Adaptation", "value": 30},
    {"from": "Prevention & Preparedness", "to": "Environmental Dimension", "value": 25},
    {"from": "Prevention & Preparedness", "to": "Cultural & Socio-economic Dimension", "value": 25},
    {"from": "Prevention & Preparedness", "to": "Health & Safety/Security Dimension", "value": 25},
    {"from": "Prevention & Preparedness", "to": "Climate Change Mitigation & Adaptation Dimension", "value": 25},
    {"from": "Detection & Response", "to": "Environmental Dimension", "value": 25},
    {"from": "Detection & Response", "to": "Cultural & Socio-economic Dimension", "value": 25},
    {"from": "Detection & Response", "to": "Health & Safety/Security Dimension", "value": 40},
    {"from": "Detection & Response", "to": "Climate Change Mitigation & Adaptation Dimension", "value": 20},
    {"from": "Restoration & Adaptation", "to": "Environmental Dimension", "value": 25},
    {"from": "Restoration & Adaptation", "to": "Cultural & Socio-economic Dimension", "value": 25},
    {"from": "Restoration & Adaptation", "to": "Health & Safety/Security Dimension", "value": 25},
    {"from": "Restoration & Adaptation", "to": "Climate Change Mitigation & Adaptation Dimension", "value": 25},

]

SANKEYCHORD_DATA_2 = [
                        {"from":"Solar", "to":"Electricity grid", "value":4},
                        {"from":"Solar", "to":"Buildings", "value":14},
                        {"from":"Solar", "to":"Losses/ own use", "value":3},
                        {"from":"Wind", "to":"Electricity grid", "value":12},
                        {"from":"Geothermal", "to":"Electricity grid", "value":2},
                        {"from":"Geothermal", "to":"Losses/ own use", "value":16},
                        {"from":"Hydro", "to":"Electricity grid", "value":23},
                        {"from":"Nuclear", "to":"Power plants", "value":36},
                        {"from":"Coal reserves", "to":"Solid", "value":184},
                        {"from":"Coal reserves", "to":"Losses/ own use", "value":38},
                        {"from":"Oil reserves", "to":"Liquid", "value":278},
                        {"from":"Oil reserves", "to":"Losses/ own use", "value":34},
                        {"from":"Gas reserves", "to":"Gas", "value":158},
                        {"from":"Gas reserves", "to":"Losses/ own use", "value":40},
                        {"from":"Biomass and waste", "to":"Solid", "value":44},
                        {"from":"Biomass and waste", "to":"Liquid", "value":7},
                        {"from":"Biomass and waste", "to":"Gas", "value":8},
                        {"from":"Biomass and waste", "to":"Losses/ own use", "value":8},
                        {"from":"Electricity grid", "to":"Buildings", "value":86},
                        {"from":"Electricity grid", "to":"Manufacturing", "value":47},
                        {"from":"Electricity grid", "to":"Transport", "value":7},
                        {"from":"Electricity grid", "to":"Other", "value":3},
                        {"from":"Electricity grid", "to":"Losses/ own use", "value":12},
                        {"from":"Solid", "to":"Buildings", "value":28},
                        {"from":"Solid", "to":"Manufacturing", "value":76},
                        {"from":"Power plants", "to":"Losses/ own use", "value":136},
                         {"from":"Liquid", "to":"Heat", "value":1},
                        {"from":"Liquid", "to":"Buildings", "value":12},
                        {"from":"Liquid", "to":"Manufacturing", "value":66},
                        {"from":"Liquid", "to":"Transport", "value":157},
                        {"from":"Liquid", "to":"Other", "value":4},
                        {"from":"Gas", "to":"Buildings", "value":35},
                        {"from":"Gas", "to":"Manufacturing", "value":48},
                        {"from":"Gas", "to":"Transport", "value":4}

                        ]

THERMOMETER = [
                {
                  "date": "2012-07-27",
                  "value": 13
                }, {
                  "date": "2012-07-28",
                  "value": 11
                }, {
                  "date": "2012-07-29",
                  "value": 15
                }, {
                  "date": "2012-07-30",
                  "value": 16
                }, {
                  "date": "2012-07-31",
                  "value": 18
                }, {
                  "date": "2012-08-01",
                  "value": 13
                }, {
                  "date": "2012-08-02",
                  "value": 22
                }, {
                  "date": "2012-08-03",
                  "value": 23
                }, {
                  "date": "2012-08-04",
                  "value": 20
                }, {
                  "date": "2012-08-05",
                  "value": 17
                }, {
                  "date": "2012-08-06",
                  "value": 16
                }, {
                  "date": "2012-08-07",
                  "value": 18
                }, {
                  "date": "2012-08-08",
                  "value": 21
                }, {
                  "date": "2012-08-09",
                  "value": 26
                }, {
                  "date": "2012-08-10",
                  "value": 24
                }, {
                  "date": "2012-08-11",
                  "value": 29
                }, {
                  "date": "2012-08-12",
                  "value": 32
                }, {
                  "date": "2012-08-13",
                  "value": 18
                }, {
                  "date": "2012-08-14",
                  "value": 24
                }, {
                  "date": "2012-08-15",
                  "value": 22
                }, {
                  "date": "2012-08-16",
                  "value": 18
                }, {
                  "date": "2012-08-17",
                  "value": 19
                }, {
                  "date": "2012-08-18",
                  "value": 14
                }, {
                  "date": "2012-08-19",
                  "value": 15
                }, {
                  "date": "2012-08-20",
                  "value": 12
                }, {
                  "date": "2012-08-21",
                  "value": 8
                }, {
                  "date": "2012-08-22",
                  "value": 9
                }, {
                  "date": "2012-08-23",
                  "value": 8
                }, {
                  "date": "2012-08-24",
                  "value": 7
                }, {
                  "date": "2012-08-25",
                  "value": 5
                }, {
                  "date": "2012-08-26",
                  "value": 11
                }, {
                  "date": "2012-08-27",
                  "value": 13
                }, {
                  "date": "2012-08-28",
                  "value": 18
                }, {
                  "date": "2012-08-29",
                  "value": 20
                }, {
                  "date": "2012-08-30",
                  "value": 29
                }, {
                  "date": "2012-08-31",
                  "value": 33
                }, {
                  "date": "2012-09-01",
                  "value": 42
                }, {
                  "date": "2012-09-02",
                  "value": 35
                }, {
                  "date": "2012-09-03",
                  "value": 31
                }, {
                  "date": "2012-09-04",
                  "value": 47
                }, {
                  "date": "2012-09-05",
                  "value": 52
                }, {
                  "date": "2012-09-06",
                  "value": 46
                }, {
                  "date": "2012-09-07",
                  "value": 41
                }, {
                  "date": "2012-09-08",
                  "value": 43
                }, {
                  "date": "2012-09-09",
                  "value": 40
                }, {
                  "date": "2012-09-10",
                  "value": 39
                }, {
                  "date": "2012-09-11",
                  "value": 34
                }, {
                  "date": "2012-09-12",
                  "value": 29
                }, {
                  "date": "2012-09-13",
                  "value": 34
                }, {
                  "date": "2012-09-14",
                  "value": 37
                }, {
                  "date": "2012-09-15",
                  "value": 42
                }, {
                  "date": "2012-09-16",
                  "value": 49
                }, {
                  "date": "2012-09-17",
                  "value": 46
                }, {
                  "date": "2012-09-18",
                  "value": 47
                }, {
                  "date": "2012-09-19",
                  "value": 55
                }, {
                  "date": "2012-09-20",
                  "value": 59
                }, {
                  "date": "2012-09-21",
                  "value": 58
                }, {
                  "date": "2012-09-22",
                  "value": 57
                }, {
                  "date": "2012-09-23",
                  "value": 61
                }, {
                  "date": "2012-09-24",
                  "value": 59
                }, {
                  "date": "2012-09-25",
                  "value": 67
                }, {
                  "date": "2012-09-26",
                  "value": 65
                }, {
                  "date": "2012-09-27",
                  "value": 61
                }, {
                  "date": "2012-09-28",
                  "value": 66
                }, {
                  "date": "2012-09-29",
                  "value": 69
                }, {
                  "date": "2012-09-30",
                  "value": 71
                }, {
                  "date": "2012-10-01",
                  "value": 67
                }, {
                  "date": "2012-10-02",
                  "value": 63
                }, {
                  "date": "2012-10-03",
                  "value": 46
                }, {
                  "date": "2012-10-04",
                  "value": 32
                }, {
                  "date": "2012-10-05",
                  "value": 21
                }, {
                  "date": "2012-10-06",
                  "value": 18
                }, {
                  "date": "2012-10-07",
                  "value": 21
                }, {
                  "date": "2012-10-08",
                  "value": 28
                }, {
                  "date": "2012-10-09",
                  "value": 27
                }, {
                  "date": "2012-10-10",
                  "value": 36
                }, {
                  "date": "2012-10-11",
                  "value": 33
                }, {
                  "date": "2012-10-12",
                  "value": 31
                }, {
                  "date": "2012-10-13",
                  "value": 30
                }, {
                  "date": "2012-10-14",
                  "value": 34
                }, {
                  "date": "2012-10-15",
                  "value": 38
                }, {
                  "date": "2012-10-16",
                  "value": 37
                }, {
                  "date": "2012-10-17",
                  "value": 44
                }, {
                  "date": "2012-10-18",
                  "value": 49
                }, {
                  "date": "2012-10-19",
                  "value": 53
                }, {
                  "date": "2012-10-20",
                  "value": 57
                }, {
                  "date": "2012-10-21",
                  "value": 60
                }, {
                  "date": "2012-10-22",
                  "value": 61
                }, {
                  "date": "2012-10-23",
                  "value": 69
                }, {
                  "date": "2012-10-24",
                  "value": 67
                }, {
                  "date": "2012-10-25",
                  "value": 72
                }, {
                  "date": "2012-10-26",
                  "value": 77
                }, {
                  "date": "2012-10-27",
                  "value": 75
                }, {
                  "date": "2012-10-28",
                  "value": 70
                }, {
                  "date": "2012-10-29",
                  "value": 72
                }, {
                  "date": "2012-10-30",
                  "value": 70
                }, {
                  "date": "2012-10-31",
                  "value": 72
                }, {
                  "date": "2012-11-01",
                  "value": 73
                }, {
                  "date": "2012-11-02",
                  "value": 67
                }, {
                  "date": "2012-11-03",
                  "value": 68
                }, {
                  "date": "2012-11-04",
                  "value": 65
                }, {
                  "date": "2012-11-05",
                  "value": 71
                }, {
                  "date": "2012-11-06",
                  "value": 75
                }, {
                  "date": "2012-11-07",
                  "value": 74
                }, {
                  "date": "2012-11-08",
                  "value": 71
                }, {
                  "date": "2012-11-09",
                  "value": 76
                }, {
                  "date": "2012-11-10",
                  "value": 77
                }, {
                  "date": "2012-11-11",
                  "value": 81
                }, {
                  "date": "2012-11-12",
                  "value": 83
                }, {
                  "date": "2012-11-13",
                  "value": 80
                }, {
                  "date": "2012-11-14",
                  "value": 81
                }, {
                  "date": "2012-11-15",
                  "value": 87
                }, {
                  "date": "2012-11-16",
                  "value": 82
                }, {
                  "date": "2012-11-17",
                  "value": 86
                }, {
                  "date": "2012-11-18",
                  "value": 80
                }, {
                  "date": "2012-11-19",
                  "value": 87
                }, {
                  "date": "2012-11-20",
                  "value": 83
                }, {
                  "date": "2012-11-21",
                  "value": 85
                }, {
                  "date": "2012-11-22",
                  "value": 84
                }, {
                  "date": "2012-11-23",
                  "value": 82
                }, {
                  "date": "2012-11-24",
                  "value": 73
                }, {
                  "date": "2012-11-25",
                  "value": 71
                }, {
                  "date": "2012-11-26",
                  "value": 75
                }, {
                  "date": "2012-11-27",
                  "value": 79
                }, {
                  "date": "2012-11-28",
                  "value": 70
                }, {
                  "date": "2012-11-29",
                  "value": 73
                }, {
                  "date": "2012-11-30",
                  "value": 61
                }, {
                  "date": "2012-12-01",
                  "value": 62
                }, {
                  "date": "2012-12-02",
                  "value": 66
                }, {
                  "date": "2012-12-03",
                  "value": 65
                }, {
                  "date": "2012-12-04",
                  "value": 73
                }, {
                  "date": "2012-12-05",
                  "value": 79
                }, {
                  "date": "2012-12-06",
                  "value": 78
                }, {
                  "date": "2012-12-07",
                  "value": 78
                }, {
                  "date": "2012-12-08",
                  "value": 78
                }, {
                  "date": "2012-12-09",
                  "value": 74
                }, {
                  "date": "2012-12-10",
                  "value": 73
                }, {
                  "date": "2012-12-11",
                  "value": 75
                }, {
                  "date": "2012-12-12",
                  "value": 70
                }, {
                  "date": "2012-12-13",
                  "value": 77
                }, {
                  "date": "2012-12-14",
                  "value": 67
                }, {
                  "date": "2012-12-15",
                  "value": 62
                }, {
                  "date": "2012-12-16",
                  "value": 64
                }, {
                  "date": "2012-12-17",
                  "value": 61
                }, {
                  "date": "2012-12-18",
                  "value": 59
                }, {
                  "date": "2012-12-19",
                  "value": 53
                }, {
                  "date": "2012-12-20",
                  "value": 54
                }, {
                  "date": "2012-12-21",
                  "value": 56
                }, {
                  "date": "2012-12-22",
                  "value": 59
                }, {
                  "date": "2012-12-23",
                  "value": 58
                }, {
                  "date": "2012-12-24",
                  "value": 55
                }, {
                  "date": "2012-12-25",
                  "value": 52
                }, {
                  "date": "2012-12-26",
                  "value": 54
                }, {
                  "date": "2012-12-27",
                  "value": 50
                }, {
                  "date": "2012-12-28",
                  "value": 50
                }, {
                  "date": "2012-12-29",
                  "value": 51
                }, {
                  "date": "2012-12-30",
                  "value": 52
                }, {
                  "date": "2012-12-31",
                  "value": 58
                }, {
                  "date": "2013-01-01",
                  "value": 60
                }, {
                  "date": "2013-01-02",
                  "value": 67
                }, {
                  "date": "2013-01-03",
                  "value": 64
                }, {
                  "date": "2013-01-04",
                  "value": 66
                }, {
                  "date": "2013-01-05",
                  "value": 60
                }, {
                  "date": "2013-01-06",
                  "value": 63
                }, {
                  "date": "2013-01-07",
                  "value": 61
                }, {
                  "date": "2013-01-08",
                  "value": 60
                }, {
                  "date": "2013-01-09",
                  "value": 65
                }, {
                  "date": "2013-01-10",
                  "value": 75
                }, {
                  "date": "2013-01-11",
                  "value": 77
                }, {
                  "date": "2013-01-12",
                  "value": 78
                }, {
                  "date": "2013-01-13",
                  "value": 70
                }, {
                  "date": "2013-01-14",
                  "value": 70
                }, {
                  "date": "2013-01-15",
                  "value": 73
                }, {
                  "date": "2013-01-16",
                  "value": 71
                }, {
                  "date": "2013-01-17",
                  "value": 74
                }, {
                  "date": "2013-01-18",
                  "value": 78
                }, {
                  "date": "2013-01-19",
                  "value": 85
                }, {
                  "date": "2013-01-20",
                  "value": 82
                }, {
                  "date": "2013-01-21",
                  "value": 83
                }, {
                  "date": "2013-01-22",
                  "value": 88
                }, {
                  "date": "2013-01-23",
                  "value": 85
                }, {
                  "date": "2013-01-24",
                  "value": 85
                }, {
                  "date": "2013-01-25",
                  "value": 80
                }, {
                  "date": "2013-01-26",
                  "value": 87
                }, {
                  "date": "2013-01-27",
                  "value": 84
                }, {
                  "date": "2013-01-28",
                  "value": 83
                }, {
                  "date": "2013-01-29",
                  "value": 84
                }, {
                  "date": "2013-01-30",
                  "value": 81
                }
         ]

HEAT_MAP_CHART_DATA2 = [
    {
        "hour": "12pm",
        "weekday": "Sun",
        "value": "0"
    },
    {
        "hour": "1am",
        "weekday": "Sun",
        "value": "1"
    },
    {
        "hour": "2am",
        "weekday": "Sun",
        "value": "2"
    },
    {
        "hour": "3am",
        "weekday": "Sun",
        "value": "1"
    },
    {
        "hour": "12pm",
        "weekday": "Mon",
        "value": "3"
    },
    {
        "hour": "1am",
        "weekday": "Mon",
        "value": "1"
    },
    {
        "hour": "2am",
        "weekday": "Mon",
        "value": "2"
    },
    {
        "hour": "3am",
        "weekday": "Mon",
        "value": "2"
    },
    {
        "hour": "12pm",
        "weekday": "Tue",
        "value": "1"
    },
    {
        "hour": "1am",
        "weekday": "Tue",
        "value": "1"
    },
    {
        "hour": "2am",
        "weekday": "Tue",
        "value": "2"
    },
    {
        "hour": "3am",
        "weekday": "Tue",
        "value": "2"
    },
    {
        "hour": "12pm",
        "weekday": "Wed",
        "value": "1"
    },
    {
        "hour": "1am",
        "weekday": "Wed",
        "value": "3"
    },
    {
        "hour": "2am",
        "weekday": "Wed",
        "value": "3"
    },
    {
        "hour": "3am",
        "weekday": "Wed",
        "value": "2"
    },
]

HEAT_MAP_CHART_DATA = [
 {
  "hour": "12pm",
  "weekday": "Sun",
  "value": 1900
 },
 {
  "hour": "1am",
  "weekday": "Sun",
  "value": 2520
 },
 {
  "hour": "2am",
  "weekday": "Sun",
  "value": 2334
 },
 {
  "hour": "3am",
  "weekday": "Sun",
  "value": 2230
 },
 {
  "hour": "4am",
  "weekday": "Sun",
  "value": 2325
 },
 {
  "hour": "5am",
  "weekday": "Sun",
  "value": 2019
 },
 {
  "hour": "6am",
  "weekday": "Sun",
  "value": 2128
 },
 {
  "hour": "7am",
  "weekday": "Sun",
  "value": 2246
 },
 {
  "hour": "8am",
  "weekday": "Sun",
  "value": 2421
 },
 {
  "hour": "9am",
  "weekday": "Sun",
  "value": 2788
 },
 {
  "hour": "10am",
  "weekday": "Sun",
  "value": 2959
 },
 {
  "hour": "11am",
  "weekday": "Sun",
  "value": 3018
 },
 {
  "hour": "12am",
  "weekday": "Sun",
  "value": 3154
 },
 {
  "hour": "1pm",
  "weekday": "Sun",
  "value": 3172
 },
 {
  "hour": "2pm",
  "weekday": "Sun",
  "value": 3368
 },
 {
  "hour": "3pm",
  "weekday": "Sun",
  "value": 3464
 },
 {
  "hour": "4pm",
  "weekday": "Sun",
  "value": 3746
 },
 {
  "hour": "5pm",
  "weekday": "Sun",
  "value": 3656
 },
 {
  "hour": "6pm",
  "weekday": "Sun",
  "value": 3336
 },
 {
  "hour": "7pm",
  "weekday": "Sun",
  "value": 3292
 },
 {
  "hour": "8pm",
  "weekday": "Sun",
  "value": 3269
 },
 {
  "hour": "9pm",
  "weekday": "Sun",
  "value": 3300
 },
 {
  "hour": "10pm",
  "weekday": "Sun",
  "value": 3403
 },
 {
  "hour": "11pm",
  "weekday": "Sun",
  "value": 3323
 },
 {
  "hour": "12pm",
  "weekday": "Mon",
  "value": 3346
 },
 {
  "hour": "1am",
  "weekday": "Mon",
  "value": 2725
 },
 {
  "hour": "2am",
  "weekday": "Mon",
  "value": 3052
 },
 {
  "hour": "3am",
  "weekday": "Mon",
  "value": 3876
 },
 {
  "hour": "4am",
  "weekday": "Mon",
  "value": 4453
 },
 {
  "hour": "5am",
  "weekday": "Mon",
  "value": 3972
 },
 {
  "hour": "6am",
  "weekday": "Mon",
  "value": 4644
 },
 {
  "hour": "7am",
  "weekday": "Mon",
  "value": 5715
 },
 {
  "hour": "8am",
  "weekday": "Mon",
  "value": 7080
 },
 {
  "hour": "9am",
  "weekday": "Mon",
  "value": 8022
 },
 {
  "hour": "10am",
  "weekday": "Mon",
  "value": 8446
 },
 {
  "hour": "11am",
  "weekday": "Mon",
  "value": 9313
 },
 {
  "hour": "12am",
  "weekday": "Mon",
  "value": 9011
 },
 {
  "hour": "1pm",
  "weekday": "Mon",
  "value": 8508
 },
 {
  "hour": "2pm",
  "weekday": "Mon",
  "value": 8515
 },
 {
  "hour": "3pm",
  "weekday": "Mon",
  "value": 8399
 },
 {
  "hour": "4pm",
  "weekday": "Mon",
  "value": 8649
 },
 {
  "hour": "5pm",
  "weekday": "Mon",
  "value": 7869
 },
 {
  "hour": "6pm",
  "weekday": "Mon",
  "value": 6933
 },
 {
  "hour": "7pm",
  "weekday": "Mon",
  "value": 5969
 },
 {
  "hour": "8pm",
  "weekday": "Mon",
  "value": 5552
 },
 {
  "hour": "9pm",
  "weekday": "Mon",
  "value": 5434
 },
 {
  "hour": "10pm",
  "weekday": "Mon",
  "value": 5070
 },
 {
  "hour": "11pm",
  "weekday": "Mon",
  "value": 4851
 },
 {
  "hour": "12pm",
  "weekday": "Tue",
  "value": 4468
 },
 {
  "hour": "1am",
  "weekday": "Tue",
  "value": 3306
 },
 {
  "hour": "2am",
  "weekday": "Tue",
  "value": 3906
 },
 {
  "hour": "3am",
  "weekday": "Tue",
  "value": 4413
 },
 {
  "hour": "4am",
  "weekday": "Tue",
  "value": 4726
 },
 {
  "hour": "5am",
  "weekday": "Tue",
  "value": 4584
 },
 {
  "hour": "6am",
  "weekday": "Tue",
  "value": 5717
 },
 {
  "hour": "7am",
  "weekday": "Tue",
  "value": 6504
 },
 {
  "hour": "8am",
  "weekday": "Tue",
  "value": 8104
 },
 {
  "hour": "9am",
  "weekday": "Tue",
  "value": 8813
 },
 {
  "hour": "10am",
  "weekday": "Tue",
  "value": 9278
 },
 {
  "hour": "11am",
  "weekday": "Tue",
  "value": 10425
 },
 {
  "hour": "12am",
  "weekday": "Tue",
  "value": 10137
 },
 {
  "hour": "1pm",
  "weekday": "Tue",
  "value": 9290
 },
 {
  "hour": "2pm",
  "weekday": "Tue",
  "value": 9255
 },
 {
  "hour": "3pm",
  "weekday": "Tue",
  "value": 9614
 },
 {
  "hour": "4pm",
  "weekday": "Tue",
  "value": 9713
 },
 {
  "hour": "5pm",
  "weekday": "Tue",
  "value": 9667
 },
 {
  "hour": "6pm",
  "weekday": "Tue",
  "value": 8774
 },
 {
  "hour": "7pm",
  "weekday": "Tue",
  "value": 8649
 },
 {
  "hour": "8pm",
  "weekday": "Tue",
  "value": 9937
 },
 {
  "hour": "9pm",
  "weekday": "Tue",
  "value": 10286
 },
 {
  "hour": "10pm",
  "weekday": "Tue",
  "value": 9175
 },
 {
  "hour": "11pm",
  "weekday": "Tue",
  "value": 8581
 },
 {
  "hour": "12pm",
  "weekday": "Wed",
  "value": 8145
 },
 {
  "hour": "1am",
  "weekday": "Wed",
  "value": 7177
 },
 {
  "hour": "2am",
  "weekday": "Wed",
  "value": 5657
 },
 {
  "hour": "3am",
  "weekday": "Wed",
  "value": 6802
 },
 {
  "hour": "4am",
  "weekday": "Wed",
  "value": 8159
 },
 {
  "hour": "5am",
  "weekday": "Wed",
  "value": 8449
 },
 {
  "hour": "6am",
  "weekday": "Wed",
  "value": 9453
 },
 {
  "hour": "7am",
  "weekday": "Wed",
  "value": 9947
 },
 {
  "hour": "8am",
  "weekday": "Wed",
  "value": 11471
 },
 {
  "hour": "9am",
  "weekday": "Wed",
  "value": 12492
 },
 {
  "hour": "10am",
  "weekday": "Wed",
  "value": 9388
 },
 {
  "hour": "11am",
  "weekday": "Wed",
  "value": 9928
 },
 {
  "hour": "12am",
  "weekday": "Wed",
  "value": 9644
 },
 {
  "hour": "1pm",
  "weekday": "Wed",
  "value": 9034
 },
 {
  "hour": "2pm",
  "weekday": "Wed",
  "value": 8964
 },
 {
  "hour": "3pm",
  "weekday": "Wed",
  "value": 9069
 },
 {
  "hour": "4pm",
  "weekday": "Wed",
  "value": 8898
 },
 {
  "hour": "5pm",
  "weekday": "Wed",
  "value": 8322
 },
 {
  "hour": "6pm",
  "weekday": "Wed",
  "value": 6909
 },
 {
  "hour": "7pm",
  "weekday": "Wed",
  "value": 5810
 },
 {
  "hour": "8pm",
  "weekday": "Wed",
  "value": 5151
 },
 {
  "hour": "9pm",
  "weekday": "Wed",
  "value": 4911
 },
 {
  "hour": "10pm",
  "weekday": "Wed",
  "value": 4487
 },
 {
  "hour": "11pm",
  "weekday": "Wed",
  "value": 4118
 },
 {
  "hour": "12pm",
  "weekday": "Thu",
  "value": 3689
 },
 {
  "hour": "1am",
  "weekday": "Thu",
  "value": 3081
 },
 {
  "hour": "2am",
  "weekday": "Thu",
  "value": 6525
 },
 {
  "hour": "3am",
  "weekday": "Thu",
  "value": 6228
 },
 {
  "hour": "4am",
  "weekday": "Thu",
  "value": 6917
 },
 {
  "hour": "5am",
  "weekday": "Thu",
  "value": 6568
 },
 {
  "hour": "6am",
  "weekday": "Thu",
  "value": 6405
 },
 {
  "hour": "7am",
  "weekday": "Thu",
  "value": 8106
 },
 {
  "hour": "8am",
  "weekday": "Thu",
  "value": 8542
 },
 {
  "hour": "9am",
  "weekday": "Thu",
  "value": 8501
 },
 {
  "hour": "10am",
  "weekday": "Thu",
  "value": 8802
 },
 {
  "hour": "11am",
  "weekday": "Thu",
  "value": 9420
 },
 {
  "hour": "12am",
  "weekday": "Thu",
  "value": 8966
 },
 {
  "hour": "1pm",
  "weekday": "Thu",
  "value": 8135
 },
 {
  "hour": "2pm",
  "weekday": "Thu",
  "value": 8224
 },
 {
  "hour": "3pm",
  "weekday": "Thu",
  "value": 8387
 },
 {
  "hour": "4pm",
  "weekday": "Thu",
  "value": 8218
 },
 {
  "hour": "5pm",
  "weekday": "Thu",
  "value": 7641
 },
 {
  "hour": "6pm",
  "weekday": "Thu",
  "value": 6469
 },
 {
  "hour": "7pm",
  "weekday": "Thu",
  "value": 5441
 },
 {
  "hour": "8pm",
  "weekday": "Thu",
  "value": 4952
 },
 {
  "hour": "9pm",
  "weekday": "Thu",
  "value": 4643
 },
 {
  "hour": "10pm",
  "weekday": "Thu",
  "value": 4393
 },
 {
  "hour": "11pm",
  "weekday": "Thu",
  "value": 4017
 },
 {
  "hour": "12pm",
  "weekday": "Fri",
  "value": 4022
 },
 {
  "hour": "1am",
  "weekday": "Fri",
  "value": 3063
 },
 {
  "hour": "2am",
  "weekday": "Fri",
  "value": 3638
 },
 {
  "hour": "3am",
  "weekday": "Fri",
  "value": 3968
 },
 {
  "hour": "4am",
  "weekday": "Fri",
  "value": 4070
 },
 {
  "hour": "5am",
  "weekday": "Fri",
  "value": 4019
 },
 {
  "hour": "6am",
  "weekday": "Fri",
  "value": 4548
 },
 {
  "hour": "7am",
  "weekday": "Fri",
  "value": 5465
 },
 {
  "hour": "8am",
  "weekday": "Fri",
  "value": 6909
 },
 {
  "hour": "9am",
  "weekday": "Fri",
  "value": 7706
 },
 {
  "hour": "10am",
  "weekday": "Fri",
  "value": 7867
 },
 {
  "hour": "11am",
  "weekday": "Fri",
  "value": 8615
 },
 {
  "hour": "12am",
  "weekday": "Fri",
  "value": 8218
 },
 {
  "hour": "1pm",
  "weekday": "Fri",
  "value": 7604
 },
 {
  "hour": "2pm",
  "weekday": "Fri",
  "value": 7429
 },
 {
  "hour": "3pm",
  "weekday": "Fri",
  "value": 7488
 },
 {
  "hour": "4pm",
  "weekday": "Fri",
  "value": 7493
 },
 {
  "hour": "5pm",
  "weekday": "Fri",
  "value": 6998
 },
 {
  "hour": "6pm",
  "weekday": "Fri",
  "value": 5941
 },
 {
  "hour": "7pm",
  "weekday": "Fri",
  "value": 5068
 },
 {
  "hour": "8pm",
  "weekday": "Fri",
  "value": 4636
 },
 {
  "hour": "9pm",
  "weekday": "Fri",
  "value": 4241
 },
 {
  "hour": "10pm",
  "weekday": "Fri",
  "value": 3858
 },
 {
  "hour": "11pm",
  "weekday": "Fri",
  "value": 3833
 },
 {
  "hour": "12pm",
  "weekday": "Sat",
  "value": 3503
 },
 {
  "hour": "1am",
  "weekday": "Sat",
  "value": 2842
 },
 {
  "hour": "2am",
  "weekday": "Sat",
  "value": 2808
 },
 {
  "hour": "3am",
  "weekday": "Sat",
  "value": 2399
 },
 {
  "hour": "4am",
  "weekday": "Sat",
  "value": 2280
 },
 {
  "hour": "5am",
  "weekday": "Sat",
  "value": 2139
 },
 {
  "hour": "6am",
  "weekday": "Sat",
  "value": 2527
 },
 {
  "hour": "7am",
  "weekday": "Sat",
  "value": 2940
 },
 {
  "hour": "8am",
  "weekday": "Sat",
  "value": 3066
 },
 {
  "hour": "9am",
  "weekday": "Sat",
  "value": 3494
 },
 {
  "hour": "10am",
  "weekday": "Sat",
  "value": 3287
 },
 {
  "hour": "11am",
  "weekday": "Sat",
  "value": 3416
 },
 {
  "hour": "12am",
  "weekday": "Sat",
  "value": 3432
 },
 {
  "hour": "1pm",
  "weekday": "Sat",
  "value": 3523
 },
 {
  "hour": "2pm",
  "weekday": "Sat",
  "value": 3542
 },
 {
  "hour": "3pm",
  "weekday": "Sat",
  "value": 3347
 },
 {
  "hour": "4pm",
  "weekday": "Sat",
  "value": 3292
 },
 {
  "hour": "5pm",
  "weekday": "Sat",
  "value": 3416
 },
 {
  "hour": "6pm",
  "weekday": "Sat",
  "value": 3131
 },
 {
  "hour": "7pm",
  "weekday": "Sat",
  "value": 3057
 },
 {
  "hour": "8pm",
  "weekday": "Sat",
  "value": 3227
 },
 {
  "hour": "9pm",
  "weekday": "Sat",
  "value": 3060
 },
 {
  "hour": "10pm",
  "weekday": "Sat",
  "value": 2855
 },
 {
  "hour": "11pm",
  "weekday": "Sat",
  "value": 11000
 }
]

PARALLEL_COORDINATES_DATA = [
    [
        "Mercury",
        4222.6,
        57.9,
        0.2408467,
        0.05527,
        4879
    ],
    [
        "Venus",
        2802,
        108.2,
        0.61519726,
        0.815,
        12104
    ],
    [
        "Earth",
        24,
        149.6,
        1.0000174,
        1,
        12756
    ],
    [
        "Mars",
        24.7,
        227.9,
        1.8808158,
        0.10745,
        6792
    ],
    [
        "Jupiter",
        9.9,
        778.6,
        11.862615,
        317.83,
        142984
    ],
    [
        "Saturn",
        10.7,
        1433.5,
        29.447498,
        95.159,
        120536
    ],
    [
        "Uranus",
        17.2,
        2872.5,
        84.016846,
        14.5,
        51118
    ],
    [
        "Neptune",
        16.1,
        4495.1,
        164.79132,
        17.204,
        49528
    ]
]


PARALLEL_COORDINATES_DATA_2 = [
                                ['Beef, round, bottom round, roast, separable lean only, trimmed to 1/8" fat, all grades, cooked', 'Beef Products', 28.0, 0.006, 0.037, 0.0, 0.0, 0.23, 0.0, 0.0, 5.72, 65.93, 163.0, 1.972, 2.391, 0.231, 31792.0],
                                ['Turkey, white, rotisserie, deli cut', 'Sausages and Luncheon Meats', 13.5, 0.016, 1.2, 0.4, 0.01, 0.349, 7.7, 4.0, 3.0, 72.0, 112.0, 0.118, 0.591, 0.37, 29432.0],
                                ['Salad dressing, buttermilk, lite', 'Fats and Oils', 1.25, 0.04, 1.12, 1.1, 0.0006, 0.132, 21.33, 3.77, 12.42, 62.04, 202.0, 1.25, 2.794, 4.213, 28256.0],
                                ['Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, select, cooked, roasted', 'Beef Products', 22.76, 0.013, 0.064, 0.0, 0.0, 0.328, 0.0, 0.0, 25.02, 50.84, 323.0, 10.05, 10.81, 0.91, 31759.0],
                                ['Pectin, liquid', 'Sweets', 0.0, 0.0, 0.0, 2.1, 0.0, 0.0, 2.1, 0.0, 0.0, 96.9, 11.0, 0.0, 0.0, 0.0, 34037.0],
                                ['Beef, chuck, arm pot roast, separable lean only, trimmed to 0" fat, choice, cooked, braised', 'Beef Products', 33.36, 0.014, 0.054, 0.0, 0.0, 0.262, 0.0, 0.0, 7.67, 58.83, 212.0, 2.903, 3.267, 0.268, 31532.0],
                                ['Nuts, chestnuts, japanese, dried', 'Nut and Seed Products', 5.25, 0.072, 0.034, 0.0, 0.0613, 0.768, 81.43, 0.0, 1.24, 9.96, 360.0, 0.183, 0.65, 0.322, 31342.0],
                                ['English muffins, mixed-grain (includes granola)', 'Baked Products', 9.1, 0.196, 0.334, 2.8, 0.0, 0.156, 46.3, 0.81, 1.8, 40.2, 235.0, 0.23, 0.827, 0.559, 33595.0],
                                ['French toast, prepared from recipe, made with low fat (2%) milk', 'Baked Products', 7.7, 0.1, 0.479, 0.0, 0.0003, 0.134, 25.0, 0.0, 10.8, 54.7, 229.0, 2.723, 4.524, 2.594, 33609.0],
                                ['Sauce, cheese sauce mix, dry', 'Soups, Sauces, and Gravies', 7.68, 0.204, 3.202, 1.0, 0.0009, 0.428, 60.52, 10.26, 18.33, 3.78, 438.0, 8.44, 6.868, 0.983, 28984.0],
                                ['Chicken, broilers or fryers, skin only, raw', 'Poultry Products', 13.33, 0.011, 0.063, 0.0, 0.0, 0.103, 0.0, 0.0, 32.35, 54.22, 349.0, 9.08, 13.54, 6.81, 28421.0],
                                ['Beef, brisket, flat half, separable lean only, trimmed to 1/8" fat, all grades, raw', 'Beef Products', 21.57, 0.016, 0.074, 0.0, 0.0, 0.336, 0.0, 0.0, 3.84, 73.76, 127.0, 1.425, 1.611, 0.166, 31466.0],
                                ['Soup, pea, low sodium, prepared with equal volume water', 'Soups, Sauces, and Gravies', 3.2, 0.012, 0.01, 1.9, 0.0006, 0.071, 9.88, 3.19, 1.09, 84.55, 62.0, 0.524, 0.372, 0.142, 29144.0],
                                ['Chilchen (Red Berry Beverage) (Navajo)', 'Ethnic Foods', 0.81, 0.007, 0.015, 0.0, 0.0, 0.028, 8.68, 2.6, 0.63, 89.69, 44.0, 0.075, 0.135, 0.151, 34928.0],
                                ['Seeds, pumpkin and squash seed kernels, dried', 'Nut and Seed Products', 30.23, 0.046, 0.007, 6.0, 0.0019, 0.809, 10.71, 1.4, 49.05, 5.23, 559.0, 8.659, 16.242, 20.976, 31403.0],
                                ['Chicken, roasting, giblets, raw', 'Poultry Products', 18.14, 0.01, 0.077, 0.0, 0.013099999999999999, 0.227, 1.14, 0.0, 5.04, 74.73, 127.0, 1.54, 1.28, 1.26, 28469.0],
                                ['Veal, shoulder, whole (arm and blade), separable lean only, raw', 'Lamb, Veal, and Game Products', 19.79, 0.022, 0.092, 0.0, 0.0, 0.311, 0.0, 0.0, 3.0, 76.58, 112.0, 0.9, 0.96, 0.31, 33271.0],
                                ['Fast foods, enchirito, with cheese, beef, and beans', 'Fast Foods', 9.27, 0.113, 0.648, 0.0, 0.0024, 0.29, 17.51, 0.0, 8.33, 62.67, 178.0, 4.118, 3.377, 0.17, 34435.0],
                                ['Beef, round, top round, steak, separable lean and fat, trimmed to 1/8" fat, all grades, raw', 'Beef Products', 22.06, 0.021, 0.06, 0.0, 0.0, 0.349, 0.0, 0.0, 7.93, 69.04, 166.0, 3.123, 3.428, 0.303, 31888.0],
                                ['Bread, pumpernickel, toasted', 'Baked Products', 9.5, 0.074, 0.738, 7.1, 0.0, 0.228, 52.2, 0.58, 3.4, 31.8, 275.0, 0.481, 1.024, 1.359, 33387.0],
                                ['Cereals, corn grits, white, regular and quick, unenriched, cooked with water, without salt', 'Breakfast Cereals', 1.42, 0.003, 0.002, 0.3, 0.0, 0.021, 12.87, 0.1, 0.19, 85.35, 59.0, 0.025, 0.048, 0.083, 29807.0],
                                ['Lamb, variety meats and by-products, brain, cooked, braised', 'Lamb, Veal, and Game Products', 12.55, 0.012, 0.134, 0.0, 0.012, 0.205, 0.0, 0.0, 10.17, 75.73, 145.0, 2.6, 1.84, 1.04, 33193.0],
                                ['Fast foods, cheeseburger; single, large patty; with condiments, vegetables and ham', 'Fast Foods', 15.55, 0.119, 0.674, 0.0, 0.0029, 0.212, 13.01, 0.0, 18.97, 50.05, 286.0, 8.317, 7.429, 1.516, 34401.0],
                                ["CAMPBELL Soup Company, CAMPBELL'S Red and White, 25% Less Sodium Cream of Mushroom Soup, condensed", 'Soups, Sauces, and Gravies', 1.61, 0.0, 0.524, 1.6, 0.0, 0.105, 6.45, 0.81, 6.45, 84.2, 89.0, 0.806, 2.419, 3.226, 28784.0],
                                ['Cereals ready-to-eat, wheat and malt barley flakes', 'Breakfast Cereals', 10.0, 0.039, 0.482, 8.8, 0.0, 0.34, 81.5, 17.6, 2.9, 3.2, 365.0, 0.6, 0.816, 1.05, 29695.0],
                                ['Cream, sour, reduced fat, cultured', 'Dairy and Egg Products', 2.94, 0.104, 0.041, 0.0, 0.0009, 0.129, 4.26, 0.16, 12.0, 80.14, 135.0, 7.47, 3.466, 0.446, 27590.0],
                                ['Pork, fresh, loin, sirloin (chops or roasts), bone-in, separable lean and fat, raw', 'Pork Products', 20.48, 0.014, 0.057, 0.0, 0.0, 0.336, 0.0, 0.0, 8.96, 70.29, 168.0, 1.851, 2.157, 0.754, 30382.0],
                                ['Wheat flour, white (industrial), 13% protein, bleached, unenriched', 'Cereal Grains and Pasta', 13.07, 0.024, 0.002, 2.4, 0.0, 0.128, 72.2, 1.1, 1.38, 12.82, 362.0, 0.189, 0.152, 0.683, 34293.0],
                                ['Fish, herring, Pacific, raw', 'Finfish and Shellfish Products', 16.39, 0.083, 0.074, 0.0, 0.0, 0.423, 0.0, 0.0, 13.88, 71.52, 195.0, 3.257, 6.872, 2.423, 32413.0],
                                ['Water, non-carbonated, bottles, natural fruit flavors, sweetened with low calorie sweetener', 'Beverages', 0.0, 0.001, 0.003, 0.0, 0.0, 0.004, 0.15, 0.0, 0.0, 99.85, 1.0, 0.0, 0.0, 0.0, 32324.0],
                                ['Babyfood, fruit, peaches, junior', 'Baby Foods', 0.94, 0.004, 0.004, 1.3, 0.0461, 0.195, 14.48, 11.5, 0.33, 83.65, 65.0, 0.02, 0.01, 0.04, 27921.0],
                                ['Alcoholic beverage, pina colada, prepared-from-recipe', 'Beverages', 0.42, 0.008, 0.006, 0.3, 0.004900000000000001, 0.071, 22.66, 22.33, 1.88, 64.99, 174.0, 1.636, 0.082, 0.033, 32092.0],
                                ['Pasta, homemade, made with egg, cooked', 'Cereal Grains and Pasta', 5.28, 0.01, 0.083, 0.0, 0.0, 0.021, 23.54, 0.0, 1.74, 68.71, 130.0, 0.408, 0.508, 0.521, 34217.0],
                                ["WENDY'S, French Fries", 'Fast Foods', 3.89, 0.015, 0.172, 3.7, 0.0050999999999999995, 0.575, 39.44, 0.0, 16.23, 38.81, 319.0, 3.201, 8.518, 3.728, 34676.0],
                                ['Beef, rib, small end (ribs 10-12), separable lean only, trimmed to 1/8" fat, select, cooked, broiled', 'Beef Products', 30.87, 0.022, 0.066, 0.0, 0.0, 0.409, 0.0, 0.0, 6.22, 62.45, 188.0, 2.369, 2.484, 0.222, 31767.0],
                                ['Turkey, fryer-roasters, back, meat and skin, cooked, roasted', 'Poultry Products', 26.15, 0.036, 0.07, 0.0, 0.0, 0.208, 0.0, 0.0, 10.24, 63.27, 204.0, 2.99, 3.53, 2.64, 28608.0],
                                ['Cereals ready-to-eat, GENERAL MILLS, Cinnamon Toast Crunch, reduced sugar', 'Breakfast Cereals', 4.9, 0.714, 0.718, 8.9, 0.02, 0.15, 77.4, 22.1, 10.2, 2.64, 381.0, 1.0, 6.8, 2.1, 29464.0],
                                ['Cookies, sugar, prepared from recipe, made with margarine', 'Baked Products', 5.9, 0.073, 0.491, 1.2, 0.0001, 0.077, 60.0, 24.86, 23.4, 8.9, 472.0, 4.69, 10.189, 7.29, 33525.0],
                                ['Fruit punch juice drink, frozen concentrate', 'Beverages', 0.3, 0.02, 0.01, 0.2, 0.0197, 0.27, 43.1, 0.0, 0.7, 55.5, 175.0, 0.087, 0.086, 0.173, 32234.0],
                                ['GREEN GIANT, HARVEST BURGER, Original Flavor, All Vegetable Protein Patties, frozen', 'Legumes and Legume Products', 20.0, 0.113, 0.457, 6.3, 0.0, 0.48, 7.8, 0.0, 4.6, 65.0, 153.0, 1.13, 2.372, 0.295, 32706.0],
                                ['Babyfood, cereal, mixed, with bananas, prepared with whole milk', 'Baby Foods', 3.82, 0.153, 0.048, 0.4, 0.0004, 0.178, 10.0, 5.9, 3.46, 81.81, 86.0, 1.808, 0.859, 0.342, 27805.0],
                                ['Gelatin desserts, dry mix, reduced calorie, with aspartame, prepared with water', 'Sweets', 0.83, 0.003, 0.048, 0.0, 0.0, 0.001, 4.22, 0.0, 0.0, 94.74, 20.0, 0.0, 0.0, 0.0, 33998.0],
                                ['Soup, chicken with rice, canned, prepared with equal volume water', 'Soups, Sauces, and Gravies', 1.45, 0.009, 0.238, 0.3, 0.0001, 0.041, 2.92, 0.08, 0.78, 93.87, 24.0, 0.185, 0.37, 0.17, 29075.0],
                                ['Fast foods, corn on the cob with butter', 'Fast Foods', 3.06, 0.003, 0.02, 0.0, 0.0047, 0.246, 21.88, 0.0, 2.35, 72.05, 106.0, 1.125, 0.688, 0.419, 34422.0],
                                ['Infant formula, PBM PRODUCTS, store brand, ready-to-feed (formerly WYETH-AYERST)', 'Baby Foods', 1.4, 0.041, 0.014, 0.0, 0.0056, 0.055, 6.39, 6.4, 3.5, 88.1, 63.0, 1.6, 1.4, 0.5, 28103.0],
                                ['Alcoholic beverage, liqueur, coffee with cream, 34 proof', 'Beverages', 2.8, 0.016, 0.092, 0.0, 0.0002, 0.032, 20.9, 19.76, 15.7, 46.5, 327.0, 9.664, 4.458, 0.669, 32088.0],
                                ['Fruit cocktail, (peach and pineapple and pear and grape and cherry), canned, juice pack, solids and liquids', 'Fruits and Fruit Juices', 0.46, 0.008, 0.004, 1.0, 0.0027, 0.095, 11.86, 10.86, 0.01, 87.44, 46.0, 0.0, 0.002, 0.004, 29947.0],
                                ["CAMPBELL Soup Company, CAMPBELL'S CHUNKY Soups, Split Pea 'N' Ham Soup", 'Soups, Sauces, and Gravies', 4.9, 0.008, 0.318, 2.0, 0.001, 0.0, 12.24, 2.04, 1.02, 81.0, 78.0, 0.408, 0.0, 0.0, 28763.0],
                                ['Beverage, Horchata, dry mix, unprepared, variety of brands, all with morro seeds', 'Beverages', 7.5, 0.06, 0.003, 4.0, 0.0003, 0.18, 79.05, 38.9, 7.46, 4.89, 413.0, 2.086, 3.174, 2.069, 32121.0],
                                ['Beans, adzuki, mature seed, cooked, boiled, with salt', 'Legumes and Legume Products', 7.52, 0.028, 0.244, 7.3, 0.0, 0.532, 24.77, 0.0, 0.1, 66.29, 128.0, 0.036, 0.0, 0.0, 32592.0],
                                ['Beans, french, mature seeds, raw', 'Legumes and Legume Products', 18.81, 0.186, 0.018, 25.2, 0.0046, 1.316, 64.11, 0.0, 2.02, 10.77, 343.0, 0.221, 0.138, 1.207, 32618.0],
                                ['Lamb, domestic, loin, separable lean and fat, trimmed to 1/8" fat, choice, cooked, roasted', 'Lamb, Veal, and Game Products', 23.27, 0.018, 0.064, 0.0, 0.0, 0.25, 0.0, 0.0, 21.12, 54.33, 290.0, 9.08, 8.65, 1.69, 33129.0],
                                ['Egg, whole, cooked, hard-boiled', 'Dairy and Egg Products', 12.58, 0.05, 0.124, 0.0, 0.0, 0.126, 1.12, 1.12, 10.61, 74.62, 155.0, 3.267, 4.077, 1.414, 27610.0],
                                ['Cereals ready-to-eat, GENERAL MILLS, CHEERIOS, Banana Nut', 'Breakfast Cereals', 5.4, 0.357, 0.57, 6.1, 0.0536, 0.252, 84.7, 33.4, 4.0, 2.2, 374.0, 0.7, 1.2, 1.9, 29454.0],
                                ['Cornmeal, self-rising, bolted, plain, enriched, yellow', 'Cereal Grains and Pasta', 8.28, 0.361, 1.247, 6.7, 0.0, 0.255, 70.28, 0.0, 3.4, 12.59, 334.0, 0.478, 0.897, 1.55, 34164.0],
                                ['Snacks, popcorn, oil-popped, white popcorn', 'Snacks', 9.0, 0.01, 0.884, 10.0, 0.0003, 0.225, 57.2, 0.0, 28.1, 2.8, 500.0, 4.89, 8.17, 13.42, 34841.0],
                                ['Kamut, uncooked', 'Cereal Grains and Pasta', 14.7, 0.024, 0.006, 9.1, 0.0, 0.446, 70.38, 8.19, 2.2, 10.95, 337.0, 0.192, 0.214, 0.616, 34177.0],
                                ['Snacks, pretzels, hard, plain, made with unenriched flour, unsalted', 'Snacks', 9.1, 0.036, 0.289, 2.8, 0.0, 0.146, 79.2, 0.0, 3.5, 3.3, 381.0, 0.75, 1.36, 1.22, 34864.0],
                                ['Fast foods, danish pastry, fruit', 'Fast Foods', 5.06, 0.023, 0.354, 0.0, 0.0017, 0.117, 47.94, 0.0, 16.95, 29.0, 356.0, 3.527, 10.74, 1.668, 34430.0],
                                ['Chicken, broilers or fryers, meat and skin and giblets and neck, cooked, fried, flour', 'Poultry Products', 28.57, 0.017, 0.086, 0.0, 0.0005, 0.237, 3.27, 0.0, 15.27, 51.88, 272.0, 4.16, 5.99, 3.51, 28395.0],
                                ['Cheese, monterey', 'Dairy and Egg Products', 24.48, 0.746, 0.536, 0.0, 0.0, 0.081, 0.68, 0.5, 30.28, 41.01, 373.0, 19.066, 8.751],
                                ['Restaurant, Chinese, fried rice', 'Restaurant Foods', 4.67, 0.014, 0.396, 1.1, 0.0, 0.088, 30.99, 0.42, 2.27, 60.99, 163.0, 0.497, 0.598, 0.947, 35087.0],
                                ['Pork, cured, ham and water product, slice, bone-in, separable lean and fat, heated, pan-broil', 'Pork Products', 19.85, 0.011, 1.188, 0.0, 0.0, 0.281, 1.41, 1.03, 7.78, 67.21, 155.0, 2.586, 3.577, 1.032, 30219.0],
                                ['Bread, protein, toasted (includes gluten)', 'Baked Products', 13.2, 0.136, 0.601, 3.3, 0.0, 0.346, 48.1, 1.44, 2.4, 34.0, 270.0, 0.364, 0.201, 1.109, 33385.0],
                                ['Cheese, dry white, queso seco', 'Dairy and Egg Products', 24.51, 0.661, 1.808, 0.0, 0.0, 0.116, 2.04, 0.55, 24.35, 42.17, 325.0, 13.718, 6.418],
                                ['Spices, thyme, dried', 'Spices and Herbs', 9.11, 1.89, 0.055, 37.0, 0.05, 0.814, 63.94, 1.71, 7.43, 7.79, 276.0, 2.73, 0.47, 1.19, 27771.0],
                                ['LITTLE CAESARS 14" Pepperoni Pizza, Large Deep Dish Crust', 'Fast Foods', 12.93, 0.201, 0.492, 1.5, 0.0, 0.173, 29.03, 3.39, 10.81, 44.98, 265.0, 4.314, 3.151, 1.756, 34535.0],
                                ['Fish, sunfish, pumpkin seed, raw', 'Finfish and Shellfish Products', 19.4, 0.08, 0.08, 0.0, 0.001, 0.35, 0.0, 0.0, 0.7, 79.5, 89.0, 0.139, 0.117, 0.246, 32511.0],
                                ['Soup, escarole, canned, ready-to-serve', 'Soups, Sauces, and Gravies', 0.62, 0.013, 1.558, 0.0, 0.0018, 0.107, 0.72, 0.0, 0.73, 96.89, 11.0, 0.22, 0.33, 0.15, 29120.0],
                                ['KRAFT CHEEZ WHIZ LIGHT Pasteurized Process Cheese Product', 'Dairy and Egg Products', 16.3, 0.418, 1.705, 0.2, 0.0004, 0.297, 16.2, 8.2, 9.5, 51.5, 215.0, 6.4, 0.0, 0.0, 27633.0],
                                ['Alcoholic beverage, wine, light', 'Beverages', 0.07, 0.009, 0.007, 0.0, 0.0, 0.088, 1.17, 1.15, 0.0, 92.23, 49.0, 0.0, 0.0, 0.0, 32102.0],
                                ['Apricots, canned, extra light syrup pack, with skin, solids and liquids', 'Fruits and Fruit Juices', 0.6, 0.01, 0.002, 1.6, 0.004, 0.14, 12.5, 0.0, 0.1, 86.3, 49.0, 0.007, 0.043, 0.02, 29869.0],
                                ['Beans, cranberry (roman), mature seeds, cooked, boiled, without salt', 'Legumes and Legume Products', 9.34, 0.05, 0.001, 10.0, 0.0, 0.387, 24.46, 0.0, 0.46, 64.65, 136.0, 0.119, 0.04, 0.199, 32614.0],
                                ['Flan, caramel custard, dry mix', 'Sweets', 0.0, 0.024, 0.432, 0.0, 0.0, 0.153, 91.6, 0.0, 0.0, 7.8, 348.0, 0.0, 0.0, 0.0, 33946.0],
                                ['USDA Commodity, salmon nuggets, cooked as purchased, unheated', 'Finfish and Shellfish Products', 11.97, 0.009, 0.167, 0.0, 0.0, 0.161, 11.85, 0.0, 10.43, 64.57, 189.0, 1.497, 4.33, 2.863, 32587.0],
                                ['Soup, scotch broth, canned, prepared with equal volume water', 'Soups, Sauces, and Gravies', 2.03, 0.008, 0.415, 0.5, 0.0004, 0.065, 3.87, 0.26, 1.07, 91.84, 33.0, 0.455, 0.315, 0.225, 29156.0],
                                ['Game meat, caribou, raw', 'Lamb, Veal, and Game Products', 22.63, 0.017, 0.057, 0.0, 0.0, 0.295, 0.0, 0.0, 3.36, 71.45, 127.0, 1.29, 1.01, 0.47, 32981.0],
                                ['Buckwheat groats, roasted, cooked', 'Cereal Grains and Pasta', 3.38, 0.007, 0.004, 2.7, 0.0, 0.088, 19.94, 0.9, 0.62, 75.63, 92.0, 0.134, 0.188, 0.188, 34145.0],
                                ['Peaches, frozen, sliced, sweetened', 'Fruits and Fruit Juices', 0.63, 0.003, 0.006, 1.8, 0.0942, 0.13, 23.98, 22.18, 0.13, 74.73, 94.0, 0.014, 0.048, 0.064, 30071.0],
                                ['KENTUCKY FRIED CHICKEN, Popcorn Chicken', 'Fast Foods', 17.67, 0.032, 1.14, 1.0, 0.0, 0.288, 21.18, 0.0, 21.74, 35.62, 351.0, 3.954, 5.66, 10.093, 34528.0],
                                ['Frostings, chocolate, creamy, dry mix, prepared with margarine', 'Sweets', 1.1, 0.012, 0.163, 1.9, 0.0, 0.143, 71.02, 0.0, 12.87, 14.07, 404.0, 1.74, 3.943, 2.797, 33951.0],
                                ['Ham, minced', 'Sausages and Luncheon Meats', 16.28, 0.01, 1.245, 0.0, 0.0, 0.311, 1.84, 0.0, 20.68, 57.35, 263.0, 7.181, 9.581, 2.47, 29276.0],
                                ['Millet, cooked', 'Cereal Grains and Pasta', 3.51, 0.003, 0.002, 1.3, 0.0, 0.062, 23.67, 0.13, 1.0, 71.41, 119.0, 0.172, 0.184, 0.508, 34191.0],
                                ['Beans, kidney, red, mature seeds, canned', 'Legumes and Legume Products', 5.26, 0.025, 0.258, 5.4, 0.0011, 0.256, 15.54, 1.86, 0.36, 77.37, 84.0, 0.085, 0.171, 0.151, 32630.0],
                                ['Pie, pumpkin, prepared from recipe', 'Baked Products', 4.5, 0.094, 0.225, 0.0, 0.0017, 0.186, 26.4, 0.0, 9.3, 58.5, 204.0, 3.171, 3.697, 1.81, 33733.0],
                                ["Syrups, chocolate, HERSHEY'S Genuine Chocolate Flavored Lite Syrup", 'Sweets', 1.4, 0.011, 0.1, 0.0, 0.0, 0.187, 34.56, 28.57, 0.97, 62.16, 153.0, 0.0, 0.0, 0.0, 34113.0],
                                ['Beef, rib, shortribs, separable lean and fat, choice, raw', 'Beef Products', 14.4, 0.009, 0.049, 0.0, 0.0, 0.232, 0.0, 0.0, 36.23, 48.29, 388.0, 15.76, 16.39, 1.32, 31743.0],
                                ['Crackers, rye, wafers, seasoned', 'Baked Products', 9.0, 0.044, 0.887, 20.9, 0.0001, 0.454, 73.8, 0.0, 9.2, 4.0, 381.0, 1.287, 3.27, 3.608, 33551.0],
                                ['Beef, rib, small end (ribs 10-12), separable lean and fat, trimmed to 1/8" fat, select, raw', 'Beef Products', 19.56, 0.022, 0.049, 0.0, 0.0, 0.297, 0.0, 0.0, 18.0, 62.0, 246.0, 7.264, 7.708, 0.685, 31760.0],
                                ['Egg, whole, dried, stabilized, glucose reduced', 'Dairy and Egg Products', 48.17, 0.222, 0.548, 0.0, 0.0, 0.515, 2.38, 0.0, 43.95, 1.87, 615.0, 13.198, 17.564, 5.713, 27615.0],
                                ['Beef, round, eye of round, roast, separable lean and fat, trimmed to 1/8" fat, select, raw', 'Beef Products', 21.3, 0.024, 0.062, 0.0, 0.0, 0.346, 0.0, 0.0, 7.57, 70.06, 159.0, 2.98, 3.271, 0.289, 31820.0],
                                ['CAMPBELL Soup Company, PREGO Pasta, Traditional Italian Sauce, ready-to-serve', 'Soups, Sauces, and Gravies', 1.54, 0.015, 0.369, 2.3, 0.0018, 0.292, 10.0, 7.69, 1.15, 80.0, 54.0, 0.0, 0.0, 0.0, 28954.0],
                                ['Bagels, cinnamon-raisin, toasted', 'Baked Products', 10.6, 0.02, 0.346, 2.5, 0.0006, 0.163, 59.3, 6.43, 1.8, 26.9, 294.0, 0.295, 0.188, 0.722, 33336.0],
                                ['Blackberry juice, canned', 'Fruits and Fruit Juices', 0.3, 0.012, 0.001, 0.1, 0.011300000000000001, 0.135, 7.8, 7.7, 0.6, 90.9, 38.0, 0.018, 0.058, 0.344, 29892.0],
                                ['Beef, chuck eye roast, boneless, America\'s Beef Roast, separable lean and fat, trimmed to 0" fat, select, cooked, roasted', 'Beef Products', 24.86, 0.019, 0.076, 0.0, 0.0, 0.312, 0.0, 0.0, 14.41, 61.29, 229.0, 6.192, 6.843, 1.2, 31498.0],
                                ['Babyfood, ravioli, cheese filled, with tomato sauce', 'Baby Foods', 3.6, 0.054, 0.282, 0.1, 0.0001, 0.032, 16.3, 0.59, 2.2, 76.5, 99.0, 0.96, 0.57, 0.48, 27984.0],
                                ["CAMPBELL Soup Company, Campbell's Pork and Beans", 'Legumes and Legume Products', 4.62, 0.031, 0.338, 5.4, 0.0, 0.0, 19.23, 6.15, 1.15, 73.7, 108.0, 0.385, 0.0, 0.0, 32664.0],
                                ['Cockles, raw (Alaska Native)', 'Ethnic Foods', 13.5, 0.03, 0.0, 0.0, 0.0, 0.0, 4.7, 0.0, 0.7, 78.8, 79.0, 0.0, 0.0, 0.0, 34933.0],
                                ['Soy protein concentrate, crude protein basis (N x 6.25), produced by acid wash', 'Legumes and Legume Products', 63.63, 0.363, 0.9, 5.5, 0.0, 0.45, 25.41, 0.0, 0.46, 5.8, 328.0, 0.052, 0.079, 0.201, 32861.0],
                                ['Turkey, light or dark meat, smoked, cooked, skin and bone removed', 'Poultry Products', 29.3, 0.025, 0.996, 0.0, 0.0, 0.298, 0.0, 0.0, 5.0, 64.9, 162.0, 1.368, 1.046, 1.408, 28644.0]
                            ]



D3_PARALLEL_COORDINATES_COLORS = [
                                     [185, 56, 73],
                                     [37, 50, 75],
                                     [325, 50, 39],
                                     [10, 28, 67],
                                     [271, 39, 57],
                                     [56, 58, 73],
                                     [28, 100, 52],
                                     [41, 75, 61],
                                     [60, 86, 61],
                                     [30, 100, 73],
                                     [318, 65, 67],
                                     [274, 30, 76],
                                     [20, 49, 49],
                                     [334, 80, 84],
                                     [185, 80, 45],
                                     [10, 30, 42],
                                     [339, 60, 49],
                                     [359, 69, 49],
                                     [204, 70, 41],
                                     [1, 100, 79],
                                     [189, 57, 75],
                                     [110, 57, 70],
                                     [214, 55, 79],
                                     [339, 60, 75],
                                     [120, 56, 40]
                    ]

HEAT_MAP_COUNTRIES_CODES = [
                            'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT',
                            'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BQ', 'BA', 'BW',
                            'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL',
                            'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ',
                            'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI',
                            'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU',
                            'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR',
                            'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW',
                            'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY',
                            'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS',
                            'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP',
                            'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA',
                            'RE', 'RO', 'RU', 'RW', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA',
                            'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK',
                            'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO',
                            'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'US', 'UM', 'UY', 'UZ', 'VU',
                            'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW'
                        ]


def generate_data_for_heat_map():
    data = []
    for country in HEAT_MAP_COUNTRIES_CODES:
        data.append(
            {
                "id": country,
             "value": randint(1, 50)
             }
        )
    return data




def generate_data_for_heat_map_chart():
    models = ["ALADIN", "FORECAST", "EU-TIMES", "LEAP", "NEMESIS", "CONTO", "MARKAL-India", "MAPLE", "NATEM",
              "SISGEMA", "TIMES-CAC", "DICE", "GCAM", "ICES", "Gemini-E3", "TIAM", "MUSE", "42", "E3ME"]
    sdgs = ["Total", "by eductional attainment level", "by age", "by sex", "by econcomic activity",
            "(Partially) Aggregated (*)", "Macroeconomic", "Private Investments", "Public investments",
            "(Partially) Aggregated (*)", "Expenditures", "Receipts", "Social benefits", "Balances",
            "(Partially) Aggregated (*)", "Production", "Value added", "Imports", "Exports", "Employment",
            "Energy expenditure", "Investments", "Raw material consumption", "Other materials consumption",
            "(Partially) Aggregated (*)", "Total gross/real disposable income", "Capital incomes", "Labour incomes",
            "Social transfers", "By quantiles", "Energy poverty", "(Partially) Aggregated (*)"]
    data = []
    for model in models:
        for sdg in sdgs:
            data.append(
                {
                    "SDG": sdg,
                    "Model": model,
                    "usage": randint(0, 100)
                }
            )
    return data


def generate_data_for_range_chart():
    vars = ["F", "BC", "NL", "C", "P"]
    data = []
    for k, var in enumerate(vars):
        for year in range(2010,2101):
            v = randint(-10, 10)
            multi_c = choice([-1, 1])
            v_c = v + multi_c * randint(0, 5)
            c_lose = v_c
            # v_p = randint((-2)*v, 2*v)
            multi_o = choice([-1, 1])
            v_p = v + multi_o * randint(0, 5)
            o_open = v_p
            data.append(
                {
                    var: v,
                    "close_"+str(k): c_lose,
                    "open_"+str(k): o_open,
                    "year_"+str(k): year
                }
            )
    return data


def generate_data_for_parallel_coordinates_chart2():
    data = []
    continents = {'Africa': ['Algeria ',
                'Angola ',
                'Benin ',
                'Botswana ',
                'Burkina Faso ',
                'Burundi ',
                'Cameroon',
                'Cape Verde ',
                'Central African Republic ',
                'Chad ',
                'Comoros ',
                'Republic of the Congo ',
                'Democratic Republic of the Congo ',
                "Côte d'Ivoire ",
                'Djibouti ',
                'Egypt  ',
                'Equatorial Guinea ',
                'Eritrea ',
                'Ethiopia ',
                'Gabon ',
                'The Gambia ',
                'Ghana ',
                'Guinea ',
                'Guinea',
                'Kenya ',
                'Lesotho ',
                'Liberia ',
                'Libya ',
                'Madagascar ',
                'Malawi ',
                'Mali ',
                'Mauritania ',
                'Mauritius ',
                'Morocco',
                'Mozambique ',
                'Namibia ',
                'Niger ',
                'Nigeria ',
                'Rwanda ',
                'São Tomé and Príncipe ',
                'Senegal ',
                'Seychelles ',
                'Sierra Leone ',
                'Somalia ',
                'South Africa ',
                'South Sudan ',
                'Sudan ',
                'Swaziland ',
                'Tanzania ',
                'Togo ',
                'Tunisia ',
                'Uganda ',
                'Western Sahara ',
                'Zambia ',
                'Zimbabwe '],
     'Asia': ['Armenia ',
              'Azerbaijan ',
              'Bahrain ',
              'Bangladesh',
              'Bhutan ',
              'Brunei ',
              'Cambodia ',
              'China ',
              'East Timor ',
              'Georgia ',
              'India ',
              'Indonesia ',
              'Iran ',
              'Iraq ',
              'Israel ',
              'Japan ',
              'Jordan ',
              'Kazakhstan ',
              'Kuwait ',
              'Kyrgyzstan ',
              'Laos ',
              'Lebanon ',
              'Malaysia ',
              'Maldives ',
              'Mongolia ',
              'Myanmar ',
              'Nepal ',
              'North Korea ',
              'Oman ',
              'Pakistan ',
              'Philippines ',
              'Palestine ',
              'Qatar ',
              'Russia ',
              'Saudi Arabia ',
              'Singapore ',
              'South Korea ',
              'Sri Lanka ',
              'Syria ',
              'Tajikistan ',
              'Thailand',
              'Turkey ',
              'Turkmenistan ',
              'Taiwan ',
              'United Arab Emirates ',
              'Uzbekistan ',
              'Vietnam ',
              'Yemen '],
     'Europe': ['Albania ',
                'Andorra ',
                'Austria ',
                'Belarus ',
                'Belgium ',
                'Bosnia and Herzegovina ',
                'Bulgaria ',
                'Croatia ',
                'Cyprus ',
                'Czech Republic ',
                'Denmark ',
                'Estonia ',
                'Finland ',
                'France ',
                'Germany ',
                'Greece ',
                'Hungary ',
                'Iceland',
                'Republic of Ireland ',
                'Italy ',
                'Kosovo',
                'Latvia ',
                'Liechtenstein ',
                'Lithuania ',
                'Luxembourg ',
                'North Macedonia ',
                'Malta ',
                'Moldova ',
                'Monaco ',
                'Montenegro ',
                'Netherlands ',
                'Norway ',
                'Poland ',
                'Portugal ',
                'Romania ',
                'Russia',
                'San Marino ',
                'Serbia ',
                'Slovakia ',
                'Slovenia ',
                'Spain ',
                'Sweden ',
                'Switzerland ',
                'Ukraine ',
                'United Kingdom ',
                'Vatican City'],
     'North America': ['Antigua and Barbuda',
                       'Anguilla',
                       'Aruba',
                       'The Bahamas',
                       'Barbados',
                       'Belize',
                       'Bermuda',
                       'Bonaire',
                       'British Virgin Islands',
                       'Canada',
                       'Cayman Islands',
                       'Clipperton Island',
                       'Costa Rica',
                       'Cuba',
                       'Curacao',
                       'Dominica',
                       'Dominican Republico',
                       'El Salvador',
                       'Greenland',
                       'Grenada',
                       'Guadeloupe',
                       'Guatemala',
                       'Haiti',
                       'Honduras',
                       'Jamaica',
                       'Martinique',
                       'Mexico',
                       'Montserrat',
                       'Navassa Island',
                       'Nicaragua',
                       'Panama',
                       'Puerto Rico',
                       'Saba',
                       'Saint Barthelemy',
                       'Saint Kitts and Nevis',
                       'Saint Lucia',
                       'Saint Martin',
                       'Saint Pierre and Miquelon',
                       'Saint Vincent and the Grenadines',
                       'Sint Eustatius',
                       'Sint Maarten',
                       'Trinidad and Tobago',
                       'Turks and Caicos',
                       'United States of America',
                       'US Virgin Islands'],
     'Ocenia': ['Australia',
                'Federated States of Micronesia',
                'Fiji',
                'Kiribati',
                'Marshall Islands',
                'New Zealand',
                'Palau',
                'Papua New Guinea',
                'Samoa',
                'Solomon Islands',
                'Tonga',
                'Tuvalu',
                'Vanuatu'],
     'South America': ['Argentina',
                       'Bolivia',
                       'Brazil',
                       'Chile',
                       'Colombia',
                       'Ecuador',
                       'French Guiana',
                       'Guyana',
                       'Paraguay',
                       'Peru',
                       'South Georgia and the South Sandwich Islands',
                       'Suriname',
                       'Uruguay',
                       'Venezuela']}
    for continent in continents:
        for country in continents[continent]:
            data.append(
                [
                    country, continent, uniform(10, 20), uniform(0, 5), uniform(20, 30)
                ]
            )
    return data
