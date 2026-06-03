# let = {
# "De":"g",
# "Da":"g",
# "Do":"g",
# "Di":"g",
# "Du":"g"
# }



# # chars = ["\uE000", "\uE001","\uE002","\uE003","\uE004","\uE005","\uE006","\uE007","\uE008","\uE009","\uE00a","\uE00b","\uE00c","\uE00d","\uE00e","\uE00f","\uE010","\uE011","\uE012","\uE013","\uE014","\uE015","\uE016","\uE017","\uE018","\uE019","\uE01a","\uE01b","\uE01c","\uE01d","\uE01e","\uE01f","\uE020","\uE021","\uE022","\uE023","\uE024","\uE025","\uE026","\uE027","\uE028","\uE029","\uE02a","\uE02b","\uE02c","\uE02d","\uE02e","\uE02f","\uE030","\uE031","\uE032","\uE033","\uE034","\uE035","\uE036","\uE037","\uE038","\uE039","\uE03a","\uE03b","\uE03c","\uE03d","\uE03e","\uE03f","\uE040","\uE041","\uE042","\uE043","\uE044","\uE045","\uE046","\uE047","\uE048","\uE049","\uE04a","\uE04b","\uE04c","\uE04d","\uE04e","\uE04f","\uE050","\uE051","\uE052","\uE053","\uE054","\uE055","\uE056","\uE057","\uE058","\uE059","\uE05a","\uE05b","\uE05c"]

# for i in let:
#     print(f"{i}:")
#     print(f"{i[0].upper()}")
#     print(f"{i[1].upper()}")
#     print(f"{let[i].upper()}")


import requests

data = requests.get("http://localhost:4000/data").json()

print(data)