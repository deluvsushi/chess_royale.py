import requests
from uuid import uuid4
from os import urandom
from hashlib import md5

class ChessRoyale:
	def __init__(self, locale: str = "en") -> None:
		self.first_api = "https://master.chessroyale.app/api/v1"
		self.second_api = "https://api-v1-master.chessroyale.app"
		self.news_api = "https://api-news.whitesharx.app/starfall"
		self.headers = {
			"user-agent": "UnityPlayer/2020.3.36f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)",
			"x-app-id": "com.xten.starfall",
			"x-app-version": "0.47.7+build.1241",
			"x-unity-version": "2020.3.36f1"
		}
		self.locale = locale
		self.player_id = None
		self.auth_token = None
		self.friend_code = None
		self.idfa = f"{uuid4()}"
		self.idfv = md5(urandom(15)).hexdigest()

	def login_as_guest(self) -> dict:
		data = {
			"locale": self.locale,
			"idfa": self.idfa,
			"idfv": self.idfv
		}
		response = requests.post(
			f"{self.first_api}/auth/guest",
			json=data,
			headers=self.headers).json()
		if "token" in response:
			self.auth_token = response["token"]
			self.player_id = response["player"]["id"]
			self.friend_code = response["player"]["code"]
			self.headers["authorization"] = self.auth_token
		return response

	def login_with_auth_token(self, auth_token: str) -> dict:
		self.auth_token = auth_token
		self.headers["authorization"] = f"Bearer {self.auth_token}"
		response = self.get_current_player()
		if "player" in response:
			self.player_id = response["player"]["id"]
			self.friend_code = response["player"]["code"]
		return response

	def check_version(self, version: str) -> dict:
		return requests.get(
			f"{self.first_api}/util/version/check?version={version}",
			headers=self.headers).json()

	def get_settings(self) -> dict:
		return requests.get(
			F"{self.first_api}/settings",
			headers=self.headers).json()

	def get_current_player(self) -> dict:
		return requests.get(
			f"{self.first_api}/players/me",
			headers=self.headers).json()

	def get_current_time(self) -> dict:
		return requests.get(
			f"{self.first_api}/util/time/current",
			headers=self.headers).json()

	def get_current_olympiads(self) -> dict:
		return requests.get(
			f"{self.first_api}/olympiads/current",
			headers=self.headers).json()


	def get_previous_olympiads(self) -> dict:
		return requests.get(
			f"{self.first_api}/olympiads/previous",
			headers=self.headers).json()

	def get_clubs_list(self) -> dict:
		return requests.get(
			f"{self.first_api}/clubs",
			headers=self.headers).json()

	def get_current_daily_mission(self) -> dict:
		return requests.get(
			f"{self.first_api}/daily_missions/current",
			headers=self.headers).json()

	def get_plays_list(
			self,
			is_finished: bool = True,
			count: int = 10) -> dict:
		return requests.get(
			f"{self.first_api}/plays?isFinished={is_finished}&count={count}",
			headers=self.headers).json()

	def get_current_rivals(self) -> dict:
		return requests.get(
			f"{self.first_api}/rivals/current",
			headers=self.headers).json()

	def get_player_info(self, player_id: str) -> dict:
		return requests.get(
			f"{self.first_api}/players/{player_id}",
			headers=self.headers).json()

	def get_player_achievements(self, player_id: str) -> dict:
		return requests.get(
			f"{self.first_api}/simple_achievements/{player_id}",
			headers=self.headers).json()

	def get_leaderboard(
			self,
			type: str = "world",
			path: str = "clubPoints") -> dict:
		return requests.get(
			f"{self.first_api}/leaderboard/{type}?path={path}",
			headers=self.headers).json()

	def get_storm_leaderboard(self) -> dict:
		return requests.get(
			f"{self.first_api}/storm/leaderboard/count",
			headers=self.headers).json()

	def get_today_storm_leaderboard(self) -> dict:
		return requests.get(
			f"{self.first_api}/storm/leaderboard/count/today",
			headers=self.headers).json()

	def get_series_storm_leaderboard(self) -> dict:
		return requests.get(
			f"{self.first_api}/storm/leaderboard/count/series",
			headers=self.headers).json()

	def get_puzzles_leaderboard(self, type: str = "world") -> dict:
		return requests.get(
			f"{self.first_api}/puzzles/leaderboard/{type}",
			headers=self.headers).json()

	def get_achievements_list(self) -> dict:
		return requests.get(
			f"{self.second_api}/achievements",
			headers=self.headers).json()

	def change_flag(self, flag_icon: int) -> dict:
		data = {
			"flagIcon": flag_icon
		}
		return requests.put(
			f"{self.first_api}/players/me/flag",
			json=data,
			headers=self.headers).json()

	def change_nickname(self, nickname: str) -> dict:
		data = {
			"nickname": nickname
		}
		return requests.put(
			f"{self.first_api}/players/me/nickname",
			json=data,
			headers=self.headers).json()

	def get_news_list(self) -> dict:
		return requests.get(
			f"{self.news_api}/{self.locale}/articles",
			headers=self.headers).json()

	def get_coin_reward(self, reward_number: int) -> dict:
		return requests.patch(
			f"{self.second_api}/rewarded/watch/{reward_number}",
			headers=self.headers).json()

	def spin_wheel(self) -> dict:
		return requests.get(
			f"{self.first_api}/wheel/ad/twist",
			headers=self.headers).json()

	def get_shop(self) -> dict:
		return requests.get(
			f"{self.first_api}/shop",
			headers=self.headers).json()
			
	def get_shop_coins(self) -> dict:
		return requests.get(
			f"{self.first_api}/shop/coins",
			headers=self.headers).json()
			
	def get_shop_hints(self) -> dict:
		return requests.get(
			f"{self.first_api}/shop/hints",
			headers=self.headers).json()

	def get_shop_avatars(self) -> dict:
		return requests.get(
			f"{self.first_api}/shop/avatars",
			headers=self.headers).json()
	
	def get_shop_phrases(self) -> dict:
		return requests.get(
			f"{self.first_api}/shop/hints/phrases",
			headers=self.headers).json()
	
	def get_shop_emoticons(self) -> dict:
		return requests.get(
			f"{self.first_api}/shop/emoticons",
			headers=self.headers).json()
	
	def get_shop_boosters(self) -> dict:
		return requests.get(
			f"{self.first_api}/shop/boosters",
			headers=self.headers).json()
	
	def get_shop_boards(self) -> dict:
		return requests.get(
			f"{self.first_api}/shop/boards",
			headers=self.headers).json()
	
	def get_shop_safes(self) -> dict:
		return requests.get(
			f"{self.first_api}/shop/safes",
			headers=self.headers).json()
	
	def get_shop_passes(self) -> dict:
		return requests.get(
			f"{self.first_api}/shop/passes",
			headers=self.headers).json()
	

	def buy_item(
			self,
			category: str,
			item_id: str) -> dict:
		return requests.post(
			f"{self.first_api}/shop/{category}/{item_id}",
			headers=self.headers).json()

	def claim_achievement(
			self,
			type: str,
			degree: int) -> dict:
		data = {
			"type": type,
			"degree": degree
		}
		return requests.post(
			f"{self.second_api}/achievements",
			json=data,
			headers=self.headers).json()

	def change_image_url(self, image_url: str) -> dict:
		data = {
			"imageUrl": image_url
		}
		return requests.put(
			f"{self.first_api}/players/me/image_url",
			json=data,
			headers=self.headers).json()
