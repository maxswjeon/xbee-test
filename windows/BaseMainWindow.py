# fmt: off

import wx
import wx.xrc

class BaseMainWindow (wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size(800, 450), style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.Title = "XBee Range Test"
		self.SetMinClientSize(wx.Size(800, 450))
		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		self.SetBackgroundColour(wx.Colour(255, 255, 255))

		sizer_root = wx.GridBagSizer(0, 0)
		sizer_root.SetFlexibleDirection(wx.BOTH)
		sizer_root.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.label_serial = wx.StaticText(self, wx.ID_ANY, u"Serial Port", wx.DefaultPosition, wx.Size(72,-1), 0)
		self.label_serial.Wrap(-1)

		sizer_root.Add(self.label_serial, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

		list_serial = []
		self.combobox_serial = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_serial, 0)
		self.combobox_serial.SetSelection(0)
		sizer_root.Add(self.combobox_serial, wx.GBPosition(0, 1), wx.GBSpan(1, 3), wx.ALL | wx.EXPAND, 5)

		self.button_refresh = wx.Button(self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer_root.Add(self.button_refresh, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

		self.button_serial = wx.Button(self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer_root.Add(self.button_serial, wx.GBPosition(0, 5), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

		group_server = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Server"), wx.VERTICAL)

		self.desc_server = wx.StaticText(group_server.GetStaticBox(), wx.ID_ANY, u"Server configurations", wx.DefaultPosition, wx.Size(-1,-1), 0)
		self.desc_server.Wrap(-1)

		group_server.Add(self.desc_server, 0, wx.ALL, 5)

		sizer_server = wx.BoxSizer(wx.HORIZONTAL)

		self.label_server = wx.StaticText(group_server.GetStaticBox(), wx.ID_ANY, u"Server URL", wx.DefaultPosition, wx.Size(72,-1), 0)
		self.label_server.Wrap(-1)

		sizer_server.Add(self.label_server, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.textbox_server = wx.TextCtrl(group_server.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		sizer_server.Add(self.textbox_server, 1, wx.ALL | wx.EXPAND, 5)

		self.button_server = wx.Button(group_server.GetStaticBox(), wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer_server.Add(self.button_server, 0, wx.ALL, 5)


		group_server.Add(sizer_server, 1, wx.EXPAND, 5)


		sizer_root.Add(group_server, wx.GBPosition(1, 0), wx.GBSpan(2, 6), wx.EXPAND, 5)

		group_metadata = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Metadata"), wx.VERTICAL)

		self.desc_metadata = wx.StaticText(group_metadata.GetStaticBox(), wx.ID_ANY, u"Experiment Metadata", wx.DefaultPosition, wx.DefaultSize, 0)
		self.desc_metadata.Wrap(-1)

		group_metadata.Add(self.desc_metadata, 0, wx.ALL, 5)

		sizer_metadata = wx.BoxSizer(wx.HORIZONTAL)

		self.label_module_id = wx.StaticText(group_metadata.GetStaticBox(), wx.ID_ANY, u"Module ID", wx.DefaultPosition, wx.Size(72,-1), 0)
		self.label_module_id.Wrap(-1)

		sizer_metadata.Add(self.label_module_id, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.textbox_module_id = wx.TextCtrl(group_metadata.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		sizer_metadata.Add(self.textbox_module_id, 1, wx.ALL | wx.EXPAND, 5)

		self.label_distance = wx.StaticText(group_metadata.GetStaticBox(), wx.ID_ANY, u"Distance", wx.DefaultPosition, wx.Size(72,-1), 0)
		self.label_distance.Wrap(-1)

		sizer_metadata.Add(self.label_distance, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.textbox_distance = wx.TextCtrl(group_metadata.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		sizer_metadata.Add(self.textbox_distance, 1, wx.ALL | wx.EXPAND, 5)


		group_metadata.Add(sizer_metadata, 1, wx.EXPAND, 5)

		sizer_notes = wx.BoxSizer(wx.HORIZONTAL)

		self.label_notes = wx.StaticText(group_metadata.GetStaticBox(), wx.ID_ANY, u"Notes", wx.DefaultPosition, wx.Size(72,-1), 0)
		self.label_notes.Wrap(-1)

		sizer_notes.Add(self.label_notes, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.textbox_notes = wx.TextCtrl(group_metadata.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		sizer_notes.Add(self.textbox_notes, 1, wx.ALL | wx.EXPAND, 5)


		group_metadata.Add(sizer_notes, 1, wx.EXPAND, 5)

		sizer_metadata_ctl = wx.BoxSizer(wx.HORIZONTAL)


		sizer_metadata_ctl.Add((0, 0), 1, wx.EXPAND, 5)

		self.button_metadata_save = wx.Button(group_metadata.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer_metadata_ctl.Add(self.button_metadata_save, 0, wx.ALL, 5)

		self.button_metadata_reset = wx.Button(group_metadata.GetStaticBox(), wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer_metadata_ctl.Add(self.button_metadata_reset, 0, wx.ALL, 5)


		group_metadata.Add(sizer_metadata_ctl, 1, wx.EXPAND, 5)


		sizer_root.Add(group_metadata, wx.GBPosition(3, 0), wx.GBSpan(4, 6), wx.EXPAND, 5)

		group_file = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"File"), wx.HORIZONTAL)

		self.label_file = wx.StaticText(group_file.GetStaticBox(), wx.ID_ANY, u"Local Data Folder", wx.DefaultPosition, wx.DefaultSize, 0)
		self.label_file.Wrap(-1)

		group_file.Add(self.label_file, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.folder_file = wx.DirPickerCtrl(group_file.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
		group_file.Add(self.folder_file, 1, wx.ALL | wx.EXPAND, 5)


		sizer_root.Add(group_file, wx.GBPosition(7, 0), wx.GBSpan(1, 6), wx.EXPAND, 5)

		sizer_ctl = wx.BoxSizer(wx.HORIZONTAL)

		sizer_stats = wx.GridSizer(2, 6, 0, 0)

		self.stats = []
		for _ in range(6):
			label = wx.StaticText(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
			label.Wrap(-1)

			sizer_stats.Add(label, 0, wx.ALL, 5)
			
			text = wx.StaticText(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
			text.Wrap(-1)

			sizer_stats.Add(text, 0, wx.ALL, 5)

			self.stats.append((label, text))


		sizer_ctl.Add(sizer_stats, 2, wx.EXPAND, 5)


		sizer_ctl.Add((0, 0), 1, wx.EXPAND, 5)

		sizer_ctl_button = wx.BoxSizer(wx.VERTICAL)

		self.button_clear = wx.Button(self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer_ctl_button.Add(self.button_clear, 0, wx.ALL, 5)

		self.button_start = wx.Button(self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer_ctl_button.Add(self.button_start, 0, wx.ALL, 5)


		sizer_ctl.Add(sizer_ctl_button, 0, wx.EXPAND, 5)


		sizer_root.Add(sizer_ctl, wx.GBPosition(8, 0), wx.GBSpan(1, 6), wx.EXPAND, 5)


		sizer_root.AddGrowableCol(1)

		self.SetSizer(sizer_root)
		self.Layout()
		self.statusbar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

		self.Centre(wx.BOTH)

	def __del__(self):
		pass
