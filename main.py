import sys
import ctypes

import dearpygui.dearpygui as dpg


def main():
    if sys.platform == "win32":
        ctypes.windll.shcore.SetProcessDpiAwareness(2)

    dpg.create_context()
    dpg.create_viewport()
    dpg.setup_dearpygui()

    with dpg.font_registry():
        with dpg.font(
            "./fonts/Pretendard-Regular.ttf", 72, default_font=True
        ) as pretendard:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Korean)

            dpg.bind_font(pretendard)
            dpg.set_global_font_scale(18 / 72)
        with dpg.font(
            "./fonts/Pretendard-Bold.ttf", 72, default_font=False
        ) as pretendardBold:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Korean)

    dpg.show_font_manager()

    with dpg.window(label="XBee Range Test", tag="MainWindow"):
        dpg.add_text("XBee Range Test Module", tag="Title")
        dpg.bind_item_font("Title", pretendardBold)

    dpg.show_viewport()
    dpg.set_primary_window("MainWindow", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
