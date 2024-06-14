#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: Bima
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import radar
import sip



class generateFmcw2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "generateFmcw2")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_up = samp_up = 2**14
        self.samp_rate = samp_rate = 32000
        self.sweep_freq = sweep_freq = samp_rate/2
        self.samp_down = samp_down = samp_up
        self.samp_cw = samp_cw = 2**14
        self.center_freq = center_freq = 3.1e9
        self.velocity = velocity = 50
        self.value_range = value_range = 200
        self.v_res = v_res = samp_rate/samp_cw*3e8/2/center_freq
        self.range_res = range_res = 3e8/2/sweep_freq
        self.protect_samp = protect_samp = 1
        self.minOutputBuffer = minOutputBuffer = int((samp_up+samp_down+samp_cw)*2)
        self.meas_duration = meas_duration = (samp_cw+samp_up+samp_down)/float(samp_rate)
        self.maxOutputBuffer = maxOutputBuffer = 0
        self.decim_fac = decim_fac = 2**5

        ##################################################
        # Blocks
        ##################################################

        self._velocity_range = qtgui.Range(0, 100, 1, 50, 200)
        self._velocity_win = qtgui.RangeWidget(self._velocity_range, self.set_velocity, "'velocity'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._velocity_win)
        self._value_range_range = qtgui.Range(0, 1000, 1, 200, 200)
        self._value_range_win = qtgui.RangeWidget(self._value_range_range, self.set_value_range, "range", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._value_range_win)
        self.radar_static_target_simulator_cc_0 = radar.static_target_simulator_cc([value_range], [velocity], [1e16], [0], [0], samp_rate, center_freq, -10, True, True, 'packet_len')
        self.radar_static_target_simulator_cc_0.set_min_output_buffer(minOutputBuffer)
        self.radar_signal_generator_fmcw_c_0 = radar.signal_generator_fmcw_c(samp_rate, samp_up, samp_down, samp_cw, -sweep_freq/2, sweep_freq, 1, 'packet_len')
        self.radar_signal_generator_fmcw_c_0.set_min_output_buffer(minOutputBuffer)
        self.qtgui_sink_x_1 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_HAMMING, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_1.set_update_time(1.0/1)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_1.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_1_win)
        self._protect_samp_range = qtgui.Range(0, 100, 1, 1, 200)
        self._protect_samp_win = qtgui.RangeWidget(self._protect_samp_range, self.set_protect_samp, "'protect_samp'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._protect_samp_win)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_multiply_conjugate_cc_0.set_min_output_buffer(minOutputBuffer)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0.set_min_output_buffer(minOutputBuffer)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.1, 0)
        self.analog_noise_source_x_0.set_min_output_buffer(minOutputBuffer)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.qtgui_sink_x_1, 0))
        self.connect((self.radar_signal_generator_fmcw_c_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.radar_signal_generator_fmcw_c_0, 0), (self.radar_static_target_simulator_cc_0, 0))
        self.connect((self.radar_static_target_simulator_cc_0, 0), (self.blocks_add_xx_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "generateFmcw2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_up(self):
        return self.samp_up

    def set_samp_up(self, samp_up):
        self.samp_up = samp_up
        self.set_meas_duration((self.samp_cw+self.samp_up+self.samp_down)/float(self.samp_rate))
        self.set_minOutputBuffer(int((self.samp_up+self.samp_down+self.samp_cw)*2))
        self.set_samp_down(self.samp_up)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_meas_duration((self.samp_cw+self.samp_up+self.samp_down)/float(self.samp_rate))
        self.set_sweep_freq(self.samp_rate/2)
        self.set_v_res(self.samp_rate/self.samp_cw*3e8/2/self.center_freq)
        self.qtgui_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.radar_static_target_simulator_cc_0.setup_targets([self.value_range], [self.velocity], [1e16], [0], [0], self.samp_rate, self.center_freq, -10, True, True)

    def get_sweep_freq(self):
        return self.sweep_freq

    def set_sweep_freq(self, sweep_freq):
        self.sweep_freq = sweep_freq
        self.set_range_res(3e8/2/self.sweep_freq)

    def get_samp_down(self):
        return self.samp_down

    def set_samp_down(self, samp_down):
        self.samp_down = samp_down
        self.set_meas_duration((self.samp_cw+self.samp_up+self.samp_down)/float(self.samp_rate))
        self.set_minOutputBuffer(int((self.samp_up+self.samp_down+self.samp_cw)*2))

    def get_samp_cw(self):
        return self.samp_cw

    def set_samp_cw(self, samp_cw):
        self.samp_cw = samp_cw
        self.set_meas_duration((self.samp_cw+self.samp_up+self.samp_down)/float(self.samp_rate))
        self.set_minOutputBuffer(int((self.samp_up+self.samp_down+self.samp_cw)*2))
        self.set_v_res(self.samp_rate/self.samp_cw*3e8/2/self.center_freq)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.set_v_res(self.samp_rate/self.samp_cw*3e8/2/self.center_freq)
        self.radar_static_target_simulator_cc_0.setup_targets([self.value_range], [self.velocity], [1e16], [0], [0], self.samp_rate, self.center_freq, -10, True, True)

    def get_velocity(self):
        return self.velocity

    def set_velocity(self, velocity):
        self.velocity = velocity
        self.radar_static_target_simulator_cc_0.setup_targets([self.value_range], [self.velocity], [1e16], [0], [0], self.samp_rate, self.center_freq, -10, True, True)

    def get_value_range(self):
        return self.value_range

    def set_value_range(self, value_range):
        self.value_range = value_range
        self.radar_static_target_simulator_cc_0.setup_targets([self.value_range], [self.velocity], [1e16], [0], [0], self.samp_rate, self.center_freq, -10, True, True)

    def get_v_res(self):
        return self.v_res

    def set_v_res(self, v_res):
        self.v_res = v_res

    def get_range_res(self):
        return self.range_res

    def set_range_res(self, range_res):
        self.range_res = range_res

    def get_protect_samp(self):
        return self.protect_samp

    def set_protect_samp(self, protect_samp):
        self.protect_samp = protect_samp

    def get_minOutputBuffer(self):
        return self.minOutputBuffer

    def set_minOutputBuffer(self, minOutputBuffer):
        self.minOutputBuffer = minOutputBuffer

    def get_meas_duration(self):
        return self.meas_duration

    def set_meas_duration(self, meas_duration):
        self.meas_duration = meas_duration

    def get_maxOutputBuffer(self):
        return self.maxOutputBuffer

    def set_maxOutputBuffer(self, maxOutputBuffer):
        self.maxOutputBuffer = maxOutputBuffer

    def get_decim_fac(self):
        return self.decim_fac

    def set_decim_fac(self, decim_fac):
        self.decim_fac = decim_fac




def main(top_block_cls=generateFmcw2, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
