import requests
import pandas as pd
from datetime import datetime

class DotaStatsParser:
    def __init__(self):
        self.base_url = "https://api.opendota.com/api"
    
    def get_match_stats(self, match_id):
        """Получение детальной статистики матча"""
        url = f"{self.base_url}/matches/{match_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении данных: {e}")
            return None
    
    def parse_player_stats(self, match_data):
        """Парсинг статистики игроков из данных матча"""
        players_data = []
        
        for player in match_data.get('players', []):
            player_stats = {
                'match_id': match_data['match_id'],
                'player_slot': player['player_slot'],
                'hero_id': player['hero_id'],
                'kills': player['kills'],
                'deaths': player['deaths'],
                'assists': player['assists'],
                'gold_per_min': player['gold_per_min'],
                'xp_per_min': player['xp_per_min'],
                'last_hits': player['last_hits'],
                'denies': player['denies'],
                'hero_damage': player['hero_damage'],
                'tower_damage': player['tower_damage'],
                'hero_healing': player['hero_healing'],
                'level': player['level']
            }
            players_data.append(player_stats)
        
        return players_data
    
    def get_hero_name(self, hero_id):
        """Получение имени героя по ID"""
        url = f"{self.base_url}/heroes"
        response = requests.get(url)
        heroes = response.json()
        
        for hero in heroes:
            if hero['id'] == hero_id:
                return hero['localized_name']
        return "Unknown"

parser = DotaStatsParser()
match_data = parser.get_match_stats(1234567890)

if match_data:
    player_stats = parser.parse_player_stats(match_data)
    df = pd.DataFrame(player_stats)
    print(df.head())

