records = []


def add_attendance():
    date = input("날짜를 입력하세요 (예: 2025-11-02): ").strip()
    name = input("이름을 입력하세요: ").strip()

    if not date or not name:
        print("날짜와 이름은 비워둘 수 없습니다.")
        return

    for record in records:
        if record["date"] == date and record["name"] == name:
            print("이미 등록된 출석입니다.")
            return

    records.append({"date": date, "name": name})
    print("출석이 저장되었습니다.")


def show_attendance():
    if not records:
        print("아직 출석 기록이 없습니다.")
        return

    print("\n출석 목록")
    for i, record in enumerate(records, start=1):
        print(f"{i}. {record['date']} - {record['name']}")


def main():
    while True:
        print("\n=== 스터디 출석부 ===")
        print("1. 출석 추가")
        print("2. 출석 목록 보기")
        print("3. 종료")

        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            add_attendance()
        elif choice == "2":
            show_attendance()
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")


main()