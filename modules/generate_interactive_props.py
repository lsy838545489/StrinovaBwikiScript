# modules/generate_interactive_props.py
import os
from utils.common import load_json_file, format_lua_table, export_data_file


def export_interactive_props_data():
    print("开始处理互动道具(InteractiveProps)数据喵...")

    custom_keys = {
        "id": "id",
        "name": "name",
        "quality": "quality",
        "file": "file",
        "get": "get",
        "desc": "desc"
    }

    InteractiveProps_data = load_json_file("InteractiveProps")
    if not InteractiveProps_data:
        return

    output_data = []
    for item in InteractiveProps_data:
        for row in item['Rows'].values():
            item_id = row['Id']

            gain_param2 = row.get('GainParam2', {})
            raw_get_str = gain_param2.get('LocalizedString', '')
            gain_param2_value = [raw_get_str] if raw_get_str else []

            extracted_data = {
                "id": item_id,
                "name": row['InteractivepropsName'].get('LocalizedString', ''),
                "quality": row['Quality'],
                "get": gain_param2_value,
                "desc": row['Content'].get('LocalizedString', '')
            }
            custom_data = {
                custom_keys[key]: value for key, value in extracted_data.items()}

            output_data.append(custom_data)

    export_data_file("InteractiveProps", output_data, fileType='json')
    export_data_file("InteractiveProps", format_lua_table(output_data), fileType='lua')
    print("互动道具(InteractiveProps)数据处理完成喵！")
