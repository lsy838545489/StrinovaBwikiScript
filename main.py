# main.py
from modules.generate_role_skin import export_role_skin_data
from modules.generate_role_skill import export_role_skill_data
from modules.generate_growth import (
    export_growth_bomb_data,
    export_growth_escort_data,
    export_growth_hotzone_data
)
from modules.generate_mascot_head import export_mascot_head_data
from modules.generate_lottery import export_lottery_data
from modules.generate_items import export_items_data
from modules.generate_interactive_props import export_interactive_props_data
from modules.generate_Id_card import export_id_card_data
from modules.generate_emote import export_emote_data
from modules.generate_decal import export_decal_data
from modules.generate_chat_bubbles import export_chat_bubbles_data
from modules.generate_badge import export_badge_data
from modules.generate_achievement import export_achievement_data
import sys
import os

# 确保能正确引入模块
PROJECT_ROOT = r"Z:\GitHub\StrinovaBwikiScript"
sys.path.append(PROJECT_ROOT)


def main_menu():
    actions = {
        "1": export_role_skin_data,
        "2": export_role_skill_data,
        "3": export_growth_bomb_data,
        "4": export_growth_escort_data,
        "5": export_growth_hotzone_data,
        "6": export_badge_data,
        "7": export_chat_bubbles_data,
        "8": export_decal_data,
        "9": export_emote_data,
        "10": export_items_data,
        "11": export_interactive_props_data,
        "12": export_id_card_data,
        "13": export_lottery_data,
        "14": export_achievement_data,
        "15": export_mascot_head_data,
    }
    while True:
        print("\n" + "=" * 40)
        print("  WIKI 数据整理与自动化上传工具  ")
        print("=" * 40)
        print("1. 生成角色时装数据 (RoleSkin)")
        print("2. 生成角色技能数据 (RoleSkill)")
        print("3. 生成爆破模式数据 (Growth_Bomb)")
        print("4. 生成极限推进数据 (Growth_Escort)")
        print("5. 生成弦区争夺模式数据 (Growth_Hotzone)")
        print("6. 生成徽章数据 (Badge)")
        print("7. 生成聊天气泡数据 (ChatBubbles)")
        print("8. 生成喷漆数据 (Decal)")
        print("9. 生成表情数据 (Emote)")
        print("10. 生成道具数据 (Items)")
        print("11. 生成互动道具数据 (InteractiveProps)")
        print("12. 生成名片封装数据 (IdCard)")
        print("13. 生成抽奖数据 (Lottery)")
        print("14. 生成并上传成就与印迹数据 (Achievement)")
        print("15. 生成头套数据 (MascotHead)")


        print("0. 退出程序")
        print("=" * 40)

        choice = input("请输入对应的数字执行任务喵: ").strip()

        if choice == "0":
            print("再见喵！")
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print("输入无效，请重新输入喵！")


if __name__ == "__main__":
    main_menu()
