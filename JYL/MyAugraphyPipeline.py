# import libraries
from augraphy import *


def my_augraphy_pipeline():
    # initialize phases and pipeline
    # ink phase with single usage of OneOf function
    ink_phase = [
        # OneOf(
        #     [
        #         InkBleed(p=0.5),
        #         InkMottling(p=0.5),
        #     ],
        #     p=1,
        # )
    ]

    paper_phase = [
        Brightness(p=0.25),
        BrightnessTexturize(p=0.25),
        DelaunayTessellation(p=0.25),
        Dithering(p=0.25),
        Jpeg(p=0.25),
        LensFlare(p=0.25),
        LightingGradient(p=0.25),
        LowLightNoise(p=0.25),
        NoiseTexturize(p=0.25),
        PatternGenerator(p=0.25),
        ShadowCast(p=0.25),
        SubtleNoise(p=0.25),
        VoronoiTessellation(p=0.25),
    ]

    # post phase with two nested OneOf function inside another OneOf function.
    post_phase = [
        OneOf([DirtyDrum(), DirtyRollers(), DirtyScreen()], p=0.25),
        Geometric(
            scale=(0.5, 1.5),
            fliplr=1,
            flipud=1,
            crop=(),
            rotate_range=(0, 360),
            p=0.5,
        ),
    ]

    # initialize pipeline
    pipeline = AugraphyPipeline(
        ink_phase=ink_phase, paper_phase=paper_phase, post_phase=post_phase
    )

    return pipeline


def my_augraphy_pipeline1():
    # initialize phases and pipeline
    # ink phase with single usage of OneOf function
    ink_phase = []

    paper_phase = [
        # 노이즈 추가 (ChatGPT 추천)
        AugmentationSequence(
            [
                NoiseTexturize(
                    sigma_range=(10, 50),
                    turbulence_range=(10, 50),
                ),
                SubtleNoise(),
            ],
            p=1,
        ),
        Jpeg(
            quality_range=(5, 10),
            p=1,
        ),
        # 기타 효과 적용
        Brightness(p=0.25),
        BrightnessTexturize(p=0.25),
        DelaunayTessellation(p=0.25),
        Dithering(p=0.25),
        LensFlare(p=0.25),
        LightingGradient(p=0.25),
        LowLightNoise(p=0.25),
        NoiseTexturize(p=0.25),
        PatternGenerator(p=0.25),
        ShadowCast(p=0.25),
        SubtleNoise(p=0.25),
        VoronoiTessellation(p=0.25),
    ]

    # post phase with two nested OneOf function inside another OneOf function.
    post_phase = [
        OneOf([DirtyDrum(), DirtyRollers(), DirtyScreen()], p=0.25),
    ]

    # initialize pipeline
    pipeline = AugraphyPipeline(
        ink_phase=ink_phase, paper_phase=paper_phase, post_phase=post_phase
    )

    return pipeline


def my_augraphy_pipeline2():
    # initialize phases and pipeline
    # ink phase with single usage of OneOf function
    ink_phase = []

    paper_phase = [
        # 노이즈 추가 (ChatGPT 추천)
        AugmentationSequence(
            [
                NoiseTexturize(
                    sigma_range=(10, 50),
                    turbulence_range=(10, 50),
                ),
                SubtleNoise(),
            ],
            p=1,
        ),
        Jpeg(
            quality_range=(5, 10),
            p=1,
        ),
        # 기타 효과 적용
        Brightness(p=0.25),
        BrightnessTexturize(p=0.25),
        DelaunayTessellation(p=0.25),
        Dithering(p=0.25),
        LensFlare(p=0.25),
        LightingGradient(p=0.25),
        LowLightNoise(p=0.25),
        NoiseTexturize(p=0.25),
        PatternGenerator(p=0.25),
        ShadowCast(p=0.25),
        SubtleNoise(p=0.25),
        VoronoiTessellation(p=0.25),
    ]

    # post phase with two nested OneOf function inside another OneOf function.
    post_phase = [
        OneOf([DirtyDrum(), DirtyRollers(), DirtyScreen()], p=0.25),
    ]

    # initialize pipeline
    pipeline = AugraphyPipeline(
        ink_phase=ink_phase, paper_phase=paper_phase, post_phase=post_phase
    )

    return pipeline


def my_augraphy_pipeline3():
    pass


def my_augraphy_pipeline4():
    pass


def my_augraphy_pipeline5():
    pass
