from __future__ import print_function
import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np

def main():
    quokka = ia.quokka(size=0.5)
    h, w = quokka.shape[0:2]
    c = 4
    segmap = np.zeros((h, w, c), dtype=np.float32)
    segmap[70:120, 90:150, 0] = 1.0
    segmap[30:70, 50:65, 1] = 1.0
    segmap[20:50, 55:85, 2] = 1.0
    segmap[120:140, 0:20, 3] = 1.0

    segmap = ia.SegmentationMapOnImage(segmap, quokka.shape)

    print("Affine...")
    aug = iaa.Affine(translate_px={"x": 20}, mode="constant", cval=128)
    quokka_aug = aug.augment_image(quokka)
    segmaps_aug = aug.augment_segmentation_maps([segmap])[0]
    segmaps_drawn = segmap.draw_on_image(quokka)
    segmaps_aug_drawn = segmaps_aug.draw_on_image(quokka_aug)

    ia.imshow(
        np.hstack([
            segmaps_drawn,
            segmaps_aug_drawn
        ])
    )

    print("Affine with mode=edge...")
    aug = iaa.Affine(translate_px={"x": 20}, mode="edge")
    quokka_aug = aug.augment_image(quokka)
    segmaps_aug = aug.augment_segmentation_maps([segmap])[0]
    segmaps_drawn = segmap.draw_on_image(quokka)
    segmaps_aug_drawn = segmaps_aug.draw_on_image(quokka_aug)

    ia.imshow(
        np.hstack([
            segmaps_drawn,
            segmaps_aug_drawn
        ])
    )

    print("PiecewiseAffine...")
    aug = iaa.PiecewiseAffine(scale=0.04)
    aug_det = aug.to_deterministic()
    quokka_aug = aug_det.augment_image(quokka)
    segmaps_aug = aug_det.augment_segmentation_maps([segmap])[0]
    segmaps_drawn = segmap.draw_on_image(quokka)
    segmaps_aug_drawn = segmaps_aug.draw_on_image(quokka_aug)

    ia.imshow(
        np.hstack([
            segmaps_drawn,
            segmaps_aug_drawn
        ])
    )

    print("PerspectiveTransform...")
    aug = iaa.PerspectiveTransform(scale=0.04)
    aug_det = aug.to_deterministic()
    quokka_aug = aug_det.augment_image(quokka)
    segmaps_aug = aug_det.augment_segmentation_maps([segmap])[0]
    segmaps_drawn = segmap.draw_on_image(quokka)
    segmaps_aug_drawn = segmaps_aug.draw_on_image(quokka_aug)

    ia.imshow(
        np.hstack([
            segmaps_drawn,
            segmaps_aug_drawn
        ])
    )

    print("ElasticTransformation alpha=3, sig=0.5...")
    aug = iaa.ElasticTransformation(alpha=3.0, sigma=0.5)
    aug_det = aug.to_deterministic()
    quokka_aug = aug_det.augment_image(quokka)
    segmaps_aug = aug_det.augment_segmentation_maps([segmap])[0]
    segmaps_drawn = segmap.draw_on_image(quokka)
    segmaps_aug_drawn = segmaps_aug.draw_on_image(quokka_aug)

    ia.imshow(
        np.hstack([
            segmaps_drawn,
            segmaps_aug_drawn
        ])
    )

    print("ElasticTransformation alpha=10, sig=3...")
    aug = iaa.ElasticTransformation(alpha=10.0, sigma=3.0)
    aug_det = aug.to_deterministic()
    quokka_aug = aug_det.augment_image(quokka)
    segmaps_aug = aug_det.augment_segmentation_maps([segmap])[0]
    segmaps_drawn = segmap.draw_on_image(quokka)
    segmaps_aug_drawn = segmaps_aug.draw_on_image(quokka_aug)

    ia.imshow(
        np.hstack([
            segmaps_drawn,
            segmaps_aug_drawn
        ])
    )

    print("CopAndPad mode=constant...")
    aug = iaa.CropAndPad(px=(-10, 10, 15, -15), pad_mode="constant", pad_cval=128)
    aug_det = aug.to_deterministic()
    quokka_aug = aug_det.augment_image(quokka)
    segmaps_aug = aug_det.augment_segmentation_maps([segmap])[0]
    segmaps_drawn = segmap.draw_on_image(quokka)
    segmaps_aug_drawn = segmaps_aug.draw_on_image(quokka_aug)

    ia.imshow(
        np.hstack([
            segmaps_drawn,
            segmaps_aug_drawn
        ])
    )

    print("CropAndPad mode=edge...")
    aug = iaa.CropAndPad(px=(-10, 10, 15, -15), pad_mode="edge")
    aug_det = aug.to_deterministic()
    quokka_aug = aug_det.augment_image(quokka)
    segmaps_aug = aug_det.augment_segmentation_maps([segmap])[0]
    segmaps_drawn = segmap.draw_on_image(quokka)
    segmaps_aug_drawn = segmaps_aug.draw_on_image(quokka_aug)

    ia.imshow(
        np.hstack([
            segmaps_drawn,
            segmaps_aug_drawn
        ])
    )

    print("Scale...")
    aug = iaa.Scale(0.5, interpolation="nearest")
    aug_det = aug.to_deterministic()
    quokka_aug = aug_det.augment_image(quokka)
    segmaps_aug = aug_det.augment_segmentation_maps([segmap])[0]
    segmaps_drawn = segmap.draw_on_image(quokka)
    segmaps_aug_drawn = segmaps_aug.draw_on_image(quokka_aug)

    ia.imshow(ia.draw_grid([segmaps_drawn, segmaps_aug_drawn], cols=2))

    print("Alpha...")
    aug = iaa.Alpha(0.7, iaa.Affine(rotate=20))
    aug_det = aug.to_deterministic()
    quokka_aug = aug_det.augment_image(quokka)
    segmaps_aug = aug_det.augment_segmentation_maps([segmap])[0]
    segmaps_drawn = segmap.draw_on_image(quokka)
    segmaps_aug_drawn = segmaps_aug.draw_on_image(quokka_aug)

    ia.imshow(
        np.hstack([
            segmaps_drawn,
            segmaps_aug_drawn
        ])
    )

if __name__ == "__main__":
    main()
