from augraphy import *


def my_pipeline1():

    ink_phase = [
        Geometric(
            padding=[0, 0, 0.05, 0],
            randomize=0,
        ),
        BindingsAndFasteners(
            overlay_types="darken",
            effect_type="punch_holes",
            width_range="random",
            height_range="random",
            ntimes=(3, 3),
            nscales=(1.0, 1.0),
            edge="top",
            edge_offset=(0.01, 0.01),
        ),
        InkBleed(
            intensity_range=(0.1, 0.2),
            kernel_size=(3, 3),
            severity=(0.2, 0.2),
        ),
    ]

    paper_phase = [
        PageBorder(
            page_border_width_height=(0, 2),
            page_border_color=(0, 0, 0),
            page_border_background_color=(0, 0, 0),
            page_numbers=1,
            page_rotation_angle_range=(0, 0),
            curve_frequency=(2, 8),
            curve_height=(2, 4),
            curve_length_one_side=(50, 100),
            same_page_border=0,
        ),
        Scribbles(
            scribbles_type="text",
            scribbles_ink="pen",
            scribbles_location=(0.9, 0.75),
            scribbles_size_range=(700, 700),
            scribbles_count_range=(1, 1),
            scribbles_thickness_range=(1, 1),
            scribbles_brightness_change=[96],
            scribbles_color=(0, 0, 0),
            scribbles_text="600",
            scribbles_text_font="random",
            scribbles_text_rotate_range=(30, 30),
        ),
        Geometric(
            translation=(-0.1, 0.2),
            randomize=0,
        ),
        Geometric(
            translation=(0, -0.05),
            randomize=0,
        ),
    ]

    post_phase = [
        Geometric(
            rotate_range=(-1, -1),
            randomize=0,
        ),
        Faxify(
            monochrome=1,
            monochrome_method="threshold_otsu",
            halftone=0,
        ),
        Brightness(
            brightness_range=(2.0, 2.0),
            min_brightness=1,
            min_brightness_value=(50, 50),
        ),
        Gamma(
            gamma_range=(1.5, 1.5),
        ),
        Letterpress(
            n_samples=(1000, 1000),
            n_clusters=(500, 500),
            std_range=(400, 400),
            value_range=(200, 255),
            value_threshold_range=(255, 255),
            blur=0,
        ),
        Scribbles(
            scribbles_type="text",
            scribbles_ink="pencil",
            scribbles_location=(0.5, 0.95),
            scribbles_size_range=(700, 700),
            scribbles_count_range=(1, 1),
            scribbles_thickness_range=(1, 1),
            scribbles_brightness_change=[0],
            scribbles_skeletonize=0,
            scribbles_color=(0, 0, 0),
            scribbles_text="P·142",
            scribbles_text_font="random",
            scribbles_text_rotate_range=(3, 3),
        ),
        BadPhotoCopy(
            noise_type=5,
            noise_side="bottom",
            noise_iteration=(1, 1),
            noise_size=(5, 7),
            noise_value=(64, 128),
            noise_sparsity=(0.2, 0.2),
            noise_concentration=(0.2, 0.2),
            blur_noise=0,
            wave_pattern=0,
            edge_effect=0,
        ),
        BadPhotoCopy(
            noise_type=1,
            noise_side="none",
            noise_iteration=(2, 3),
            noise_size=(1, 4),
            noise_value=(0, 64),
            noise_sparsity=(0.5, 0.6),
            noise_concentration=(0.01, 0.01),
            blur_noise=0,
            wave_pattern=0,
            edge_effect=0,
        ),
    ]

    pipeline = AugraphyPipeline(
        ink_phase=ink_phase, paper_phase=paper_phase, post_phase=post_phase
    )

    return pipeline
