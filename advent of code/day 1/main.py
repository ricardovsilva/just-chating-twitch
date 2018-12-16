from chronal_calibrator import ChronalCalibrator


with open("sample.txt") as file:
    content = file.readlines()
    sanitized_content = [line.replace('\n', '') for line in content]
    darth_bane = ChronalCalibrator()
    result = darth_bane.calibrate(', '.join(sanitized_content))
    print(result)
