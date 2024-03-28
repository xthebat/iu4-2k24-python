from dataclasses import dataclass, field


@dataclass
class BoneInitData:
	bone_id: int
	bone_name: str
	bone_parent_id: int

	@classmethod
	def from_string(cls, bone_string: str):
		"""
		Method that fills bone data from string from SMD file
		:param bone_string: text line with bone information
		"""
		bone_fields = bone_string.split()

		if len(bone_fields) != 3:
			raise ValueError(f"Error in BoneData: {bone_string}")

		return cls(int(bone_fields[0]), bone_fields[1], int(bone_fields[2]))

	def to_string(self) -> str:
		"""
		Method that returns bone data in SMD format
		:return: text line with bone data
		"""
		return f"{self.bone_id} {self.bone_name} {self.bone_parent_id}"


@dataclass
class BonePositionData:
	bone_id: int
	bone_x: float
	bone_y: float
	bone_z: float
	bone_pitch: float
	bone_yaw: float
	bone_roll: float

	@classmethod
	def from_string(cls, bone_position_string: str):
		"""
		Method that fills bone position data in time frame from string from SMD file
		:param bone_position_string: text line with bone position information
		"""

		bone_position_data = bone_position_string.split()

		if len(bone_position_data) != 7:
			raise ValueError(f"Error in BonePositionData {bone_position_string}")

		bone_position_fields = map(float, bone_position_data[1:])

		return cls(int(bone_position_data[0]), *bone_position_fields)

	def to_string(self) -> str:
		"""
		Method that returns bone position data in SMD format
		:return: text line with bone position data
		"""
		return (f"{self.bone_id} {self.bone_x:.6f} {self.bone_y:.6f} {self.bone_z:.6f} "
		        f"{self.bone_pitch:.6f} {self.bone_yaw:.6f} {self.bone_roll:.6f}\n")


@dataclass
class FrameData:
	frame_id: int
	frame_position_data: dict[int, BonePositionData] = field(default_factory=dict)

	@classmethod
	def from_string(cls, frame_string: str):
		frame_string_data = frame_string.split()

		if frame_string_data[0] != "time":
			raise ValueError(f"Error in frame string {frame_string}")

		return cls(int(frame_string_data[1]))

	def to_string(self) -> str:
		"""
		Method that returns frame data in SMD format
		:return: text line with frame data
		"""
		for bone_id in sorted(self.frame_position_data.keys()):
			yield self.frame_position_data[bone_id].to_string()
