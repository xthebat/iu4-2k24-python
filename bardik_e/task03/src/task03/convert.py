import os.path

from task03.structures import *


class AbstractConverter:
	def __init__(self, doc):
		pass

	def convert(self):
		raise NotImplementedError

	def save(self):
		raise NotImplementedError


class MovementSMDConverter(AbstractConverter):
	def __init__(self, doc: SMDDocument):
		AbstractConverter.__init__(self, doc)

		self.document = doc
		self.file_path = os.path.join(os.getcwd(), "converted.smd")

	def convert(self):
		"""
		Method that converts the SMD document. As a result, the model moving will be removed.
		"""
		start_frame = self.document.frames[min(self.document.frames.keys())]

		for frame_id in self.document.frames.keys():
			for bone_id in self.document.frames[frame_id].frame_position_data.keys():
				self.document.frames[frame_id].frame_position_data[bone_id].bone_x = (
					start_frame.frame_position_data[bone_id].bone_x)
				self.document.frames[frame_id].frame_position_data[bone_id].bone_y = (
					start_frame.frame_position_data[bone_id].bone_y)

	def save(self) -> str:
		"""
		Method that saves the converted SMD document from internal representation to file.
		:return: path of written file
		"""
		try:
			with open(self.file_path, "wt+") as output_file:
				output_file.writelines(self.document.out_string())

			return self.file_path

		except PermissionError:
			raise PermissionError("Unable to open file for converted output.")
