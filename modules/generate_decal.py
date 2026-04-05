# modules/generate_decal.py
import os
from utils.common import load_json_file, format_lua_table, export_data_file


def export_decal_data():
    print("开始处理喷漆(Decal)数据喵...")
    custom_keys = {
        "ID": "id",
        "Name": "name",
        "Quality": "quality",
        "Get": "get",
        "Desc": "desc",
    }

    Decal_data = load_json_file("Decal")
    if not Decal_data:
        return

    output_data = []
    for item in Decal_data:
        for row in item["Rows"].values():
            gain_param2 = row.get("GainParam2", {})
            raw_get_str = gain_param2.get("LocalizedString", "")
            gain_param2_value = [raw_get_str] if raw_get_str else []

            Desc_string = row["Desc"].get(
                "LocalizedString", "").replace("\n", "")

            extracted_data = {
                "ID": row["Id"],
                "Name": row["Name"].get("LocalizedString", ""),
                "Quality": row["Quality"],
                "Get": gain_param2_value,
                "Desc": Desc_string,
            }
            custom_data = {
                custom_keys[key]: value for key, value in extracted_data.items()
            }

            output_data.append(custom_data)

    export_data_file("Decal", output_data, fileType='json')
    export_data_file("Decal", format_lua_table(output_data), fileType='lua')
    print("喷漆(Decal)数据处理完成喵！")
