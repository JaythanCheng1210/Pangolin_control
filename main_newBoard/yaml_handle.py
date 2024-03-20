import yaml
lab_file_path = '/home/ubuntu/ArmPi/HiwonderSDK/PWMServo/yaml/lab_config.yaml'
Deviation_file_path = '/home/ubuntu/ArmPi/HiwonderSDK/PWMServo/yaml/Deviation.yaml'
PickingCoordinates_file_path = '/home/ubuntu/ArmPi/HiwonderSDK/PWMServo/yaml/PickingCoordinates.yaml'

def get_yaml_data(yaml_file):
    file = open(yaml_file, 'r', encoding='utf-8')
    file_data = file.read()
    file.close()
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    
    return data

def save_yaml_data(data, yaml_file):
    file = open(yaml_file, 'w', encoding='utf-8')
    yaml.dump(data, file)
    file.close()
