import os
import cv2


class ImageFeatures:
    def preprocess_image(self, image_path):
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (256, 256), interpolation=cv2.INTER_CUBIC)
        equalized = cv2.equalizeHist(resized)

        return equalized

    def calculate_moment_invariants(self, image_path):
        preprocessed_image = self.__preprocess_image(image_path)
        moments = cv2.moments(preprocessed_image)

        eta20 = moments['mu20'] / moments['m00']**2
        eta02 = moments['mu02'] / moments['m00']**2
        eta11 = moments['mu11'] / moments['m00']**2
        eta30 = moments['mu30'] / moments['m00']**2
        eta12 = moments['mu12'] / moments['m00']**2
        eta21 = moments['mu21'] / moments['m00']**2
        eta03 = moments['mu03'] / moments['m00']**2

        phi1 = eta20 + eta02
        phi2 = (eta20 - eta02)**2 + 4 * eta11**2
        phi3 = (eta30 - 3 * eta12)**2 + (3 * eta21 - eta03)**2

        return phi1, phi2, phi3
