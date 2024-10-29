import unittest
import os
import random
# from src.HAlphaAnomalyzer.anomalyzer import Anomalyzer


class TestAnomalyzer(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([2, 2]), 4, "Should be 4")

    # def test_anova_method(self):
    #     anomalous_folder_path = '../_data_for_demo/_anomalous_images'
    #     non_anomalous_folder_path = '../_data_for_demo/_non-anomalous_images'
    #
    #     # Normalize the folder paths to current OS
    #     anomalous_folder_path = os.path.normpath(anomalous_folder_path)
    #     non_anomalous_folder_path = os.path.normpath(non_anomalous_folder_path)
    #
    #     # Get paths of all anomalous images in a list
    #     anomalous_paths = [
    #         os.path.join(anomalous_folder_path, file_name)
    #         for file_name in os.listdir(anomalous_folder_path)
    #         if file_name.lower().endswith(('.jpg', '.jpeg', '.png'))
    #     ]
    #
    #     # Get paths of all non-anomalous images in a list
    #     non_anomalous_paths = [
    #         os.path.join(non_anomalous_folder_path, file_name)
    #         for file_name in os.listdir(non_anomalous_folder_path)
    #         if file_name.lower().endswith(('.jpg', '.jpeg', '.png'))
    #     ]
    #
    #     # Randomly sample anomalous and non-anomalous image paths
    #     random.seed(123)
    #     sampled_anomalous_paths = random.sample(anomalous_paths, 20)
    #     sampled_non_anomalous_paths = random.sample(non_anomalous_paths, 20)
    #     anomalyzer = Anomalyzer(grid_size=8)
    #     anomalyzer.compute_best_ranges(sampled_non_anomalous_paths, sampled_anomalous_paths, method='anova')
    #
    #     test_img_paths = ['../_data_for_demo/_anomalous_images/20111211154554Bh.jpeg',
    #                       '../_data_for_demo/_non-anomalous_images/20110114105034Ch_02.jpeg']
    #     corrupt_images_labels = anomalyzer.find_corrupt_images(test_img_paths,
    #                                                            likelihood_threshold=0.6,
    #                                                            min_corrupt_cells=5,
    #                                                            verbose=True)
    #     self.assertEqual(corrupt_images_labels, [1, 0])


if __name__ == "__main__":
    unittest.main()
