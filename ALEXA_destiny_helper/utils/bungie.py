# Dependencies
import urllib3
import json


# Constants
D2_PLATFORM_BASE_URL = "https://www.bungie.net/Platform/"
AUTH_HEADERS = {'X-API-KEY': '1a8bc70982bd413b86beca062d76bd97'}
MILESTONE_HASH = '1437935813'
MODIFIER_JSON_FILE = "./data/modifiers.json"

class Bungie:

    http = urllib3.PoolManager()
    modifier_data = []
    milestones = {}
    

    def __init__(self):
        # print("Bungie imported.")
        self.modifier_data = self.load_json_data(MODIFIER_JSON_FILE)
        # print(self.modifier_data)

    def get_strike_modifiers(self):
        milestone_data = self.get_milestones()
        modifier_hashes = self.get_modifier_hashes(milestone_data)
        modifiers = self.translate_modifier_hashes(modifier_hashes)
        
        return modifiers


    # --------------------------------------------- HELPER FUNCTIONS ---------------------------------------
    def load_json_data(self, file):
        with open(file) as f:
            data = json.load(f)

        return data

    def get_milestones(self):
        url = D2_PLATFORM_BASE_URL + "/Destiny2/Milestones/"
        
        response = self.http.request('GET', url, headers=AUTH_HEADERS)
        json_response = json.loads(response.data.decode('utf-8'))
        
        return json_response["Response"]

    def get_modifier_hashes(self, data):
        return data[MILESTONE_HASH]['activities'][0]['modifierHashes']

    def translate_modifier_hashes(self, modifiers_hash_array):
        modifiers_array = []

        for hash in modifiers_hash_array:
            # modifiers_array.append()
            modifiers_array.append( self.modifier_data[str(hash)]['displayProperties']['name'] )

        return modifiers_array

    



