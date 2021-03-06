# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mycroft.skills import MycroftSkill, intent_handler
from mycroft.skills.audioservice import AudioService


class CCRadioNewSkill(MycroftSkill):
    def initialize(self):                   
        self.audioservice = AudioService(self.bus)
            
    @intent_handler("PonCCRadio.intent")
    def handle_pon_ccradio_intent(self, message):
        self.speak_dialog("Reproducindo")
        self.audioservice.play('https://radioserver02.ccradio.es/radio/8000/radio.mp3')
        
def create_skill():
    return CCRadioNewSkill()
