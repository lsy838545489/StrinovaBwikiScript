# modules/generate_mascot_head.py
import os
from utils.common import load_json_file, export_data_file, format_lua_table


def export_mascot_head_data():
    print("开始处理头套（Mascot Head）数据喵...")

    custom_keys = {
        "id": "id",
        "name": "name",
        "quality": "quality",
        "get": "get",
        "desc": "desc"
    }

    MascotHead_data = load_json_file("MascotHead")
    if not MascotHead_data:
        return

    output_data = []
    for item in MascotHead_data:
        for row in item['Rows'].values():
            item_id = row['Id']

            gain_param2 = row.get('GainParam2', {})
            raw_get_str = gain_param2.get('LocalizedString', '')
            gain_param2_value = [raw_get_str] if raw_get_str else []

            Quality_name = row['Quality']

            Desc_string = row['Desc'].get('LocalizedString', '').replace(
                '\n', '').replace('【头套】', '')

            extracted_data = {
                "id": item_id,
                "name": row['Name'].get('LocalizedString', ''),
                "quality": Quality_name,
                "get": gain_param2_value,
                "desc": Desc_string
            }
            custom_data = {
                custom_keys[key]: value for key, value in extracted_data.items()}

            output_data.append(custom_data)

    export_data_file('MascotHead', format_lua_table(output_data), fileType='lua')
    export_data_file('MascotHead', output_data, fileType='json')
    print("头套（Mascot Head）数据处理完成喵！")
