import unittest
from unittest.mock import MagicMock, patch
from matplotlib.backends.backend_webagg_core import FigureCanvasWebAggCore


class TestFigureCanvasWebAggCore(unittest.TestCase):
    def setUp(self):
        self.figure = MagicMock()
        self.canvas = FigureCanvasWebAggCore(self.figure)

    #show method results matplotlib.pyplot.show function being called once
    def test_show(self):
        with patch("matplotlib.pyplot.show") as mock_show:
            self.canvas.show()
            mock_show.assert_called_once()

    #tests if draw method calls draw_idle once
    def test_draw(self):
        with patch.object(self.canvas, "draw_idle") as mock_draw_idle:
            self.canvas.draw()
            mock_draw_idle.assert_called_once()

    #draw_idle methond sends draw event
    def test_draw_idle(self):
        with patch.object(self.canvas, "send_event") as mock_send_event:
            self.canvas.draw_idle()
            mock_send_event.assert_called_once_with("draw")

    #refresh event triggers call to send_event and call draw_idle
    def test_handle_refresh(self):
        refresh_event = {'type': 'refresh'}
        with patch.object(self.canvas, "send_event"), \
             patch.object(self.canvas, "draw_idle") as mock_draw_idle:
            self.canvas.handle_refresh(refresh_event)
            mock_draw_idle.assert_called_once()

if __name__ == '__main__':
    unittest.main()
