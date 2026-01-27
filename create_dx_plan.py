import pandas as pd
from datetime import date

def create_dx_plan():
    # Define the data based on the provided text
    data = [
        # 1. 会議・テーマ推進 (Meetings & Theme Promotion)
        {
            "Category": "会議・テーマ推進",
            "Task": "初回打合せ (Initial Meeting)",
            "Start_Date": date(2024, 10, 1),
            "End_Date": date(2024, 11, 30),
            "Status": "Completed (実績)",
            "Progress": 1.0,
            "Notes": "10月～11月頃"
        },
        {
            "Category": "会議・テーマ推進",
            "Task": "案件精査 (Case Scrutiny)",
            "Start_Date": date(2025, 1, 1),
            "End_Date": date(2025, 2, 28),
            "Status": "Completed (実績)",
            "Progress": 1.0,
            "Notes": "1月～2月頃"
        },
        {
            "Category": "会議・テーマ推進",
            "Task": "優先順位付け・テーマ精査 (Prioritization & Refinement)",
            "Start_Date": date(2025, 2, 1),
            "End_Date": date(2025, 3, 31),
            "Status": "Completed",
            "Progress": 1.0,
            "Notes": "案件精査後、3件に絞り込み"
        },
        {
            "Category": "会議・テーマ推進",
            "Task": "テーマ始動 (Theme Start)",
            "Start_Date": date(2025, 4, 1),
            "End_Date": date(2026, 3, 31),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": "機械1G, 2G, 3G / 電計1G, 2G"
        },

        # 2. その他管理項目 (Management)
        {
            "Category": "その他管理項目",
            "Task": "BI構築 (BI Construction)",
            "Start_Date": date(2025, 4, 1),
            "End_Date": date(2026, 3, 31),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": "計画・実績枠あり"
        },
        {
            "Category": "その他管理項目",
            "Task": "DX進捗報告 (DX Progress Report)",
            "Start_Date": date(2025, 4, 1),
            "End_Date": date(2026, 3, 31),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": "定期報告"
        },

        # 3. データ連携 (Plantia v5 リスク評価)
        {
            "Category": "データ連携 (Plantia v5)",
            "Task": "データ取得 (Data Acquisition)",
            "Start_Date": date(2025, 4, 1),
            "End_Date": date(2025, 4, 30),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": "電気・計装"
        },
        {
            "Category": "データ連携 (Plantia v5)",
            "Task": "データ連携処理 (Integration Processing)",
            "Start_Date": date(2025, 5, 1),
            "End_Date": date(2025, 5, 31),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": ""
        },
        {
            "Category": "データ連携 (Plantia v5)",
            "Task": "Power Automate処理",
            "Start_Date": date(2025, 6, 1),
            "End_Date": date(2025, 6, 30),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": ""
        },
        {
            "Category": "データ連携 (Plantia v5)",
            "Task": "出力データ連携 (Output Integration)",
            "Start_Date": date(2025, 7, 1),
            "End_Date": date(2025, 7, 31),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": ""
        },
        {
            "Category": "データ連携 (Plantia v5)",
            "Task": "電計データ入力 (Data Entry)",
            "Start_Date": date(2025, 3, 1),
            "End_Date": date(2025, 3, 31),
            "Status": "Completed",
            "Progress": 1.0,
            "Notes": "担当：中馬 (推測), 完了済み"
        },

        # 4. 機器ファミリ空白問題 (Blank Issue)
        {
            "Category": "機器ファミリ空白問題",
            "Task": "データ精査アプローチ検討",
            "Start_Date": date(2025, 4, 1),
            "End_Date": date(2025, 4, 30),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": ""
        },
        {
            "Category": "機器ファミリ空白問題",
            "Task": "資料作成",
            "Start_Date": date(2025, 5, 1),
            "End_Date": date(2025, 5, 31),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": ""
        },
        {
            "Category": "機器ファミリ空白問題",
            "Task": "修繕費への織り込み",
            "Start_Date": date(2025, 6, 1),
            "End_Date": date(2025, 6, 30),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": ""
        },
        {
            "Category": "機器ファミリ空白問題",
            "Task": "編成方針・検計",
            "Start_Date": date(2025, 7, 1),
            "End_Date": date(2025, 7, 31),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": ""
        },
        {
            "Category": "機器ファミリ空白問題",
            "Task": "TL会議周知・枠予算整理",
            "Start_Date": date(2025, 8, 1),
            "End_Date": date(2025, 8, 31),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": ""
        },
        {
            "Category": "機器ファミリ空白問題",
            "Task": "効果測定",
            "Start_Date": date(2025, 9, 1),
            "End_Date": date(2026, 3, 31),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": ""
        },

        # 5. DB取り込み・外部データ連携 (DB Import)
        {
            "Category": "DB取り込み・外部データ連携",
            "Task": "保全依頼取り込み (Maintenance Request)",
            "Start_Date": date(2025, 4, 1),
            "End_Date": date(2026, 3, 31),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": "計画・実績あり (データ格納済み)"
        },
        {
            "Category": "DB取り込み・外部データ連携",
            "Task": "工場入場人員取り込み (Entry Personnel)",
            "Start_Date": date(2025, 4, 1),
            "End_Date": date(2026, 3, 31),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": "計画・実績枠あり"
        },
        {
            "Category": "DB取り込み・外部データ連携",
            "Task": "工事日報取り込み (Construction Report)",
            "Start_Date": date(2025, 4, 1),
            "End_Date": date(2026, 3, 31),
            "Status": "Planned",
            "Progress": 0.0,
            "Notes": "計画・実績枠あり"
        }
    ]

    # Create DataFrame
    df = pd.DataFrame(data)

    # Sort by Category and Start Date
    df = df.sort_values(by=['Category', 'Start_Date'])

    # File Path
    file_path = "dx_plan_2025.xlsx"

    # Write to Excel
    try:
        df.to_excel(file_path, index=False, sheet_name="DX Plan FY2025")
        print(f"Successfully created '{file_path}' with {len(df)} tasks.")
    except Exception as e:
        print(f"Error creating Excel file: {e}")

if __name__ == "__main__":
    create_dx_plan()
