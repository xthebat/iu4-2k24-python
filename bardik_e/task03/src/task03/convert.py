from task03.structures import SMDDocument


class MovementSMDConverter:
	@staticmethod
	def convert(document: SMDDocument):
		"""
		Method that converts the SMD document. As a result, the model moving will be removed.
		"""
		start_frame = document.frames[min(document.frames.keys())]

		for frame_id in document.frames:
			for bone_id in document.frames[frame_id].frame_position_data:
				document.frames[frame_id].frame_position_data[bone_id].bone_x = (
					start_frame.frame_position_data[bone_id].bone_x)
				document.frames[frame_id].frame_position_data[bone_id].bone_y = (
					start_frame.frame_position_data[bone_id].bone_y)

		return document
