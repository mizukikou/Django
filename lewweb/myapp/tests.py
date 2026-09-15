from unittest.mock import Mock, patch

from django.test import TestCase


class LinearRegressionViewTests(TestCase):
	def test_predict_page_is_available(self):
		response = self.client.get("/predict/")

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "房價預測")

	@patch("myapp.views._load_model")
	def test_predict_sends_model_features_in_expected_order(self, load_model):
		model = Mock()
		model.predict.return_value = [12345678.4]
		load_model.return_value = model

		response = self.client.post(
			"/predict/",
			{
				"area": "30",
				"age": "10",
				"rooms": "3",
				"floor": "5",
				"metro_distance": "400",
				"school_distance": "800",
				"parking": "1",
				"district": "新北市板橋區",
			},
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "12,345,678")
		model.predict.assert_called_once_with(
			[[30.0, 10.0, 3.0, 5.0, 400.0, 800.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]]
		)
