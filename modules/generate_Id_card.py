# modules/generate_Id_card.py
import os
from utils.common import load_json_file, format_lua_table, export_data_file


def export_id_card_data():
    print("开始处理名片与边框数据喵...")
    custom_keys_avatar = {
        "ID": "id",
        "Name": "name",
        "Quality": "quality",
        "File": "file",
        "Img": "img",
        "Get": "get",
        "Desc": "desc"
    }

    custom_keys_frame = {
        "ID": "id",
        "Name": "name",
        "Quality": "quality",
        "File": "file",
        "Get": "get",
        "Desc": "desc"
    }

    IdCard_data = load_json_file("IdCard")
    if not IdCard_data:
        return
    output_data_avatar = []
    output_data_frame = []

    # 处理每个条目
    for item in IdCard_data:
        for row in item.get('Rows', {}).values():
            type_value = row.get('Type', '')

            gain_param2 = row.get('GainParam2', {})
            raw_get_str = gain_param2.get('LocalizedString', '')
            gain_param2_value = [raw_get_str] if raw_get_str else []

            Icon_name = row.get('IconItem', {}).get('AssetPathName', '')
            tail_number1_1 = Icon_name.split('/')[-1].split('_')[-2]
            tail_number1_2 = Icon_name.split('/')[-1].split('_')[-1]

            Desc_string = row.get('Desc', {}).get(
                'LocalizedString', '').replace('\n', '')

            if type_value == "EPMCardResourceType::Avatar":
                Icon_Display_name = row.get(
                    'IconDisplayItem', {}).get('AssetPathName', '')
                tail_number2 = Icon_Display_name.split(
                    '_')[-1].split('.')[0] if Icon_Display_name else ''

                # 包含 Img 字段的 Avatar 类型数据
                extracted_data = {
                    "ID": row.get('Id', ''),
                    "Name": row.get('Name', {}).get('LocalizedString', ''),
                    "Quality": row['Quality'],
                    "File": f"基板_{tail_number1_1}_{tail_number1_2}.png",
                    "Img": f"基板_{tail_number2}.png",  # 包含 Img 字段
                    "Get": gain_param2_value,
                    "Desc": Desc_string
                }
                custom_data = {
                    custom_keys_avatar[key]: value for key, value in extracted_data.items()}
                output_data_avatar.append(custom_data)

            elif type_value == "EPMCardResourceType::Frame":
                extracted_data = {
                    "ID": row.get('Id', ''),
                    "Name": row.get('Name', {}).get('LocalizedString', ''),
                    "Quality": row['Quality'],
                    "File": f"封装_{tail_number1_1}_{tail_number1_2}.png",
                    "Get": gain_param2_value,
                    "Desc": Desc_string
                }
                custom_data = {
                    custom_keys_frame[key]: value for key, value in extracted_data.items()}
                output_data_frame.append(custom_data)

    export_data_file("IdCard", output_data_avatar, fileType='json')
    export_data_file("Frame", output_data_frame, fileType='json')
    export_data_file("IdCard", format_lua_table(output_data_avatar), fileType='lua')
    export_data_file("Frame", format_lua_table(output_data_frame), fileType='lua')
    print("名片与边框数据处理完成喵！\n")
