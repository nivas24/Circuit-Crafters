import os

def calculate_metrics(total_vehicles, total_vor, stk, aws, wip, awi):
    total_vehicles_without_stk = total_vehicles - stk
    
    esr = 100 - (total_vor / total_vehicles) * 100
    esr_without_stk = 100 - (total_vor / total_vehicles_without_stk) * 100
    
    ear = 100 - ((aws + wip + awi) / total_vehicles) * 100
    ear_without_stk = 100 - ((aws + wip + awi) / total_vehicles_without_stk) * 100

    return esr, esr_without_stk, ear, ear_without_stk

def main():
    # Fetch data from environment variables or defaults
    sections = [
        {
            "section": "SECTION ONE",
            "total_vehicles": int(os.getenv("SECTION_ONE_TOTAL_VEHICLES", 78)),
            "total_vor": int(os.getenv("SECTION_ONE_TOTAL_VOR", 4)),
            "stk": int(os.getenv("SECTION_ONE_STK", 1)),
            "aws": int(os.getenv("SECTION_ONE_AWS", 3)),
            "wip": int(os.getenv("SECTION_ONE_WIP", 0)),
            "awi": int(os.getenv("SECTION_ONE_AWI", 6))
        },
        {
            "section": "SECTION TWO",
            "total_vehicles": int(os.getenv("SECTION_TWO_TOTAL_VEHICLES", 61)),
            "total_vor": int(os.getenv("SECTION_TWO_TOTAL_VOR", 31)),
            "stk": int(os.getenv("SECTION_TWO_STK", 3)),
            "aws": int(os.getenv("SECTION_TWO_AWS", 9)),
            "wip": int(os.getenv("SECTION_TWO_WIP", 1)),
            "awi": int(os.getenv("SECTION_TWO_AWI", 0))
        }
    ]
    
    for section in sections:
        esr, esr_without_stk, ear, ear_without_stk = calculate_metrics(
            section["total_vehicles"],
            section["total_vor"],
            section["stk"],
            section["aws"],
            section["wip"],
            section["awi"]
        )

        print(f"*** {section['section']} ***")
        print(f"Total Vehicles: {section['total_vehicles']}")
        print(f"Total VOR: {section['total_vor']}")
        print(f"STK: {section['stk']}")
        print(f"AWS: {section['aws']}")
        print(f"WIP: {section['wip']}")
        print(f"AWI: {section['awi']}")
        print(f"ESR: {esr:.2f}%")
        print(f"EAR: {ear:.2f}%")
        print(f"ESR w/o STK: {esr_without_stk:.2f}%")
        print(f"EAR w/o STK: {ear_without_stk:.2f}%")
        print()

if __name__ == "__main__":
    main()
