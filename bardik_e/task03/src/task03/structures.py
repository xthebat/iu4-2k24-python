from task03.smd_structures import *


@dataclass
class AbstractDocument:
	def out_string(self):
		raise NotImplementedError


@dataclass
class SMDDocument(AbstractDocument):
	document_version: int = 1
	bones: dict[int, BoneInitData] = field(default_factory=dict)
	frames: dict[int, FrameData] = field(default_factory=dict)

	def out_string(self) -> str:
		"""
		Generator method that yields the document line by line.
		:return: line that will be written to file in SMD format
		"""
		yield f"version {self.document_version}\n"
		yield "nodes\n"

		for bone_id in sorted(list(self.bones.keys())):
			yield f"\t{bone_id} {self.bones[bone_id].bone_name} {self.bones[bone_id].bone_parent_id}\n"

		yield "end\n"
		yield "skeleton\n"

		for frame_id in sorted(list(self.frames.keys())):
			yield f"\ttime {frame_id}\n"

			for bone_data in self.frames[frame_id].get_out_string():
				yield f"\t\t{bone_data}"

		yield "end\n"


class AbstractDocumentFabric:
	def create_document(self, doc_string: str) -> AbstractDocument:
		raise NotImplementedError


class SMDDocumentFabric(AbstractDocumentFabric):
	def create_document(self, doc_string: str) -> SMDDocument:
		"""
		Method that creates an internal representation of the SMD document from string.
		:param doc_string: SMD document text
		:return: SMDDocument instance
		"""

		# flags that indicates which section is currently handling
		bone_section = False
		frame_section = False

		# number of handling time section
		last_frame_number = 0

		result = SMDDocument()

		for line in doc_string.split("\n"):
			if line.startswith("version"):
				result.document_version = int(line.split()[1])

			elif line.startswith("nodes"):
				bone_section = True

			elif line.startswith("skeleton"):
				frame_section = True

			elif line.startswith("end"):
				bone_section = False
				frame_section = False

			elif bone_section:
				bone_data = line.strip().split()
				result.bones[int(bone_data[0])] = BoneInitData(int(bone_data[0]), bone_data[1], int(bone_data[2]))

			elif frame_section:
				line_data = line.strip().split()

				if line_data[0] == "time":
					last_frame_number = int(line_data[1])
					result.frames[last_frame_number] = FrameData(last_frame_number)

				else:
					bone_frame_data = list(map(float, line_data))
					bone_id = int(bone_frame_data[0])

					bone_data = BonePositionData(bone_id, bone_frame_data[1], bone_frame_data[2],
						bone_frame_data[3], bone_frame_data[4], bone_frame_data[5], bone_frame_data[6])

					result.frames[last_frame_number].frame_position_data[bone_id] = bone_data

		return result
