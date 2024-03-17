import dearpygui.dearpygui as dpg


def main():
    dpg.create_context()
    dpg.create_viewport()
    dpg.setup_dearpygui()

    with dpg.font_registry():
        with dpg.font(
            "./fonts/PretendardVariable.ttf", 14, default_font=True
        ) as pretendard:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Korean)

            dpg.bind_font(pretendard)

    dpg.show_font_manager()

    with dpg.window(label="XBee Range Test", tag="MainWindow"):
        dpg.add_text("XBee Range Test Module")

    dpg.show_viewport()
    dpg.set_primary_window("MainWindow", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
