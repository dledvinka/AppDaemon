import hassapi as hass

class GoodWeController(hass.Hass):

  def initialize(self):
    self.listen_state(self.on_timestamp, "sensor.timestamp")

  def on_timestamp(self, entity, attribute, old, new, kwargs):
    self.log("Test")