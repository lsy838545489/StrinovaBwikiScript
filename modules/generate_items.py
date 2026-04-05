# modules/generate_items.py
import os
from utils.common import load_json_file, export_data_file, format_lua_table


def export_items_data():
    print("开始处理道具(Item)数据喵...")

    custom_keys = {
        "id": "id",
        "name": "name",
        "quality": "quality",
        "file": "file",
        "desc": "desc"
    }

    Item_data = load_json_file("Item")
    if not Item_data:
        return

    output_data = []

    exclude_ranges = [
        (30001, 30999),
        (50001, 55999),
        (60001, 69999),
        (80001, 89999),
        (90001, 91000),
        (93001, 93999),
        # 可继续添加其他范围...
    ]
    exclude_ids = {
        18001,
        19001,
        19101,
        19201,
        19202,
        19301
    }

    for item in Item_data:
        for row in item['Rows'].values():
            item_id = row['Id']

            if any(lower <= item_id <= upper for (lower, upper) in exclude_ranges) or item_id in exclude_ids:
                continue

            asset_path_name = row['IconItem'].get('AssetPathName', '')
            tail_number = asset_path_name.split('_')[-1].split('.')[0]

            Desc_string = row['Desc'].get(
                'LocalizedString', '').replace('\n', '<br>')

            extracted_data = {
                "id": item_id,
                "name": row['Name'].get('LocalizedString', ''),
                "quality": row['Quality'],
                "file": f"道具图标_{tail_number}.png",
                "desc": Desc_string
            }
            custom_data = {
                custom_keys[key]: value for key, value in extracted_data.items()}

            output_data.append(custom_data)

    # ===== 在保存前按 id 从小到大排序（稳健处理 id 为字符串或数字的情况） =====
    def _id_key(entry):
        v = entry.get('id', 0)
        try:
            return int(v)
        except Exception:
            try:
                return int(str(v).strip())
            except Exception:
                return 0

    output_data.sort(key=_id_key)
    # ======================================================================

    export_data_file('Items', format_lua_table(output_data), fileType='lua')
    export_data_file('Items', output_data, fileType='json')
    print("道具(Item)数据处理完成喵！")
