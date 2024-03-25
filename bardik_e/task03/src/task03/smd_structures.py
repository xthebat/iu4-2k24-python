from dataclasses import dataclass, field


@dataclass
class BoneInitData:
	bone_id: int = 0
	bone_name: str = ""
	bone_parent_id: int = -1

	def fill_with_smd_string(self, bone_string: str):
		"""
		Method that fills bone data from string from SMD file
		:param bone_string: text line with bone information
		"""
		bone_fields = bone_string.split()

		if len(bone_fields) != 3:
			raise ValueError(f"Error in BoneData: {bone_string}")

		self.bone_id, self.bone_name, self.bone_parent_id = int(bone_fields[0]), bone_fields[1], int(bone_fields[2])

	def get_out_string(self) -> str:
		"""
		Method that returns bone data in SMD format
		:return: text line with bone data
		"""
		return f"{self.bone_id} {self.bone_name} {self.bone_parent_id}"


@dataclass
class BonePositionData:
	bone_id: int = 0
	bone_x: float = 0
	bone_y: float = 0
	bone_z: float = 0
	bone_alpha: float = 0
	bone_beta: float = 0
	bone_gamma: float = 0

	def fill_with_smd_string(self, bone_position_string: str):
		"""
		Method that fills bone position data in time frame from string from SMD file
		:param bone_position_string: text line with bone position information
		"""
		bone_position_fields = bone_position_string.split()

		if len(bone_position_fields) != 7:
			raise ValueError(f"Error in BonePositionData: {bone_position_string}")

		self.bone_id, self.bone_x, self.bone_y, self.bone_z, self.bone_alpha, self.bone_beta, self.bone_gamma = (
			map(float, bone_position_fields))

	def get_out_string(self) -> str:
		"""
		Method that returns bone position data in SMD format
		:return: text line with bone position data
		"""
		return f"\
{self.bone_id} \
{self.bone_x:.6f} \
{self.bone_y:.6f} \
{self.bone_z:.6f} \
{self.bone_alpha:.6f} \
{self.bone_beta:.6f} \
{self.bone_gamma:.6f}\n"


@dataclass
class FrameData:
	frame_id: int = 0
	frame_position_data: dict[int, BonePositionData] = field(default_factory=dict)

	def get_out_string(self) -> str:
		"""
		Method that returns frame data in SMD format
		:return: text line with frame data
		"""
		for bone_id in sorted(list(self.frame_position_data.keys())):
			yield self.frame_position_data[bone_id].get_out_string()
