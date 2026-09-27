# 호환성 검사 — `pibo/260624v1`

- 기준: openpibo-os 태그 `260624v1`, openpibo `0.9.3.3.1`
- 방법: 정적 검사 (`tools/compat/check_compat.py`). **실기기 동작 확인은 별도.**
- 결과: 189개 중 OK 113 / FAIL 76

| 파일 | 종류 | 결과 | 문제 |
|---|---|---|---|
| `block/assistant/10_detect_all.json` | block | FAIL | 블록 `vision_face` 정의 없음<br>블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/assistant/13_conversation.json` | block | OK |  |
| `block/assistant/14_project.json` | block | FAIL | 블록 `device_eye_off` 정의 없음<br>블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/assistant/1_hello.json` | block | OK |  |
| `block/assistant/2_intro.json` | block | OK |  |
| `block/assistant/3_clock.json` | block | FAIL | 블록 `device_eye_off` 정의 없음 |
| `block/assistant/4_weather_collect.json` | block | OK |  |
| `block/assistant/5_news_collect.json` | block | OK |  |
| `block/assistant/6_motion_test.json` | block | OK |  |
| `block/assistant/7_weather_cast.json` | block | OK |  |
| `block/assistant/8_news_cast.json` | block | OK |  |
| `block/assistant/9_image_test.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/automove/1_hello.json` | block | OK |  |
| `block/automove/2_intro.json` | block | OK |  |
| `block/automove/3_dance.json` | block | OK |  |
| `block/automove/4_image_test.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/automove/5_predict_tm.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음<br>블록 `vision_load_tm` 정의 없음<br>블록 `vision_predict_tm` 정의 없음 |
| `block/automove/6_detect_marker.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/automove/7_automove.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/automove/8_automove_ext.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/automove/9_automove_ext2.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/basics/b_color.json` | block | OK |  |
| `block/basics/b_function.json` | block | OK |  |
| `block/basics/b_list1.json` | block | OK |  |
| `block/basics/b_list2.json` | block | OK |  |
| `block/basics/b_logic1.json` | block | OK |  |
| `block/basics/b_logic2.json` | block | OK |  |
| `block/basics/b_logic3.json` | block | OK |  |
| `block/basics/b_loop1.json` | block | OK |  |
| `block/basics/b_loop2.json` | block | OK |  |
| `block/basics/b_math.json` | block | OK |  |
| `block/basics/b_text.json` | block | OK |  |
| `block/basics/b_variable.json` | block | OK |  |
| `block/basics/p_audio.json` | block | OK |  |
| `block/basics/p_collect.json` | block | OK |  |
| `block/basics/p_device.json` | block | FAIL | 블록 `device_eye_off` 정의 없음 |
| `block/basics/p_display.json` | block | OK |  |
| `block/basics/p_motion.json` | block | OK |  |
| `block/basics/p_utils.json` | block | OK |  |
| `block/basics/p_vision1.json` | block | FAIL | 블록 `vision_classification` 정의 없음<br>블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/basics/p_vision2.json` | block | FAIL | 블록 `vision_analyze_pose` 입력 `val` 없음 ×4 |
| `block/basics/p_vision3.json` | block | FAIL | 블록 `vision_load_tm` 정의 없음<br>블록 `vision_predict_tm` 정의 없음 |
| `block/basics/p_voice.json` | block | OK |  |
| `block/botcard/bc_qr.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/botcard/bc_qr_ext.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/botcard/bc_tm.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음<br>블록 `vision_load_tm` 정의 없음<br>블록 `vision_predict_tm` 정의 없음 |
| `block/examples/audio.json` | block | OK |  |
| `block/examples/b_color.json` | block | OK |  |
| `block/examples/b_function.json` | block | OK |  |
| `block/examples/b_list1.json` | block | OK |  |
| `block/examples/b_list2.json` | block | OK |  |
| `block/examples/b_logic1.json` | block | OK |  |
| `block/examples/b_logic2.json` | block | OK |  |
| `block/examples/b_logic3.json` | block | OK |  |
| `block/examples/b_loop1.json` | block | OK |  |
| `block/examples/b_loop2.json` | block | OK |  |
| `block/examples/b_math.json` | block | OK |  |
| `block/examples/b_text.json` | block | OK |  |
| `block/examples/b_variable.json` | block | OK |  |
| `block/examples/collect.json` | block | OK |  |
| `block/examples/device.json` | block | FAIL | 블록 `device_eye_off` 정의 없음 |
| `block/examples/ex_ai1.json` | block | FAIL | 블록 `vision_classification` 정의 없음<br>블록 `vision_imshow_to_ide_img` 정의 없음 ×2 |
| `block/examples/ex_ai2.json` | block | FAIL | 블록 `vision_analyze_pose` 입력 `val` 없음 ×4<br>블록 `vision_face_age` 정의 없음<br>블록 `vision_face_gender` 정의 없음<br>블록 `vision_face` 정의 없음<br>블록 `vision_imshow_to_ide_img` 정의 없음 ×2 |
| `block/examples/ex_audio.json` | block | OK |  |
| `block/examples/ex_camera.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 ×2 |
| `block/examples/ex_dance.json` | block | FAIL | 블록 `device_eye_off` 정의 없음 |
| `block/examples/ex_face_tracking.json` | block | FAIL | 블록 `vision_face` 정의 없음<br>블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/examples/ex_greet.json` | block | FAIL | 블록 `device_eye_off` 정의 없음 |
| `block/examples/ex_image1.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 ×2 |
| `block/examples/ex_image2.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/examples/ex_led.json` | block | OK |  |
| `block/examples/ex_motor_1.json` | block | OK |  |
| `block/examples/ex_motor_2.json` | block | OK |  |
| `block/examples/ex_oled_1.json` | block | OK |  |
| `block/examples/ex_oled_2.json` | block | OK |  |
| `block/examples/ex_pir.json` | block | OK |  |
| `block/examples/ex_project.json` | block | FAIL | 블록 `vision_face` 정의 없음<br>블록 `vision_load_tm` 정의 없음<br>블록 `vision_predict_tm` 정의 없음 |
| `block/examples/ex_tm.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음<br>블록 `vision_load_tm` 정의 없음<br>블록 `vision_predict_tm` 정의 없음 |
| `block/examples/ex_touch.json` | block | OK |  |
| `block/examples/motion.json` | block | OK |  |
| `block/examples/oled.json` | block | OK |  |
| `block/examples/speech.json` | block | OK |  |
| `block/examples/vision.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/history-performance/audio.json` | block | OK |  |
| `block/history-performance/eye.json` | block | FAIL | 블록 `device_eye_fade` 정의 없음<br>블록 `device_eye_off` 정의 없음 |
| `block/history-performance/motion.json` | block | OK |  |
| `block/history-performance/oled.json` | block | OK |  |
| `block/history-performance/project.json` | block | FAIL | 블록 `device_eye_off` 정의 없음 |
| `block/history-performance/vision.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 ×3 |
| `block/history-performance/voice.json` | block | OK |  |
| `block/sign-language/detect_object.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/sign-language/eye.json` | block | OK |  |
| `block/sign-language/eye_mission.json` | block | FAIL | 블록 `device_eye_off` 정의 없음 |
| `block/sign-language/eye_rand.json` | block | OK |  |
| `block/sign-language/for.json` | block | OK |  |
| `block/sign-language/if.json` | block | OK |  |
| `block/sign-language/motion.json` | block | OK |  |
| `block/sign-language/motion_music.json` | block | OK |  |
| `block/sign-language/motion_rand.json` | block | OK |  |
| `block/sign-language/music_seq.json` | block | FAIL | 블록 `device_eye_off` 정의 없음 |
| `block/sign-language/oled_figure.json` | block | OK |  |
| `block/sign-language/oled_img.json` | block | OK |  |
| `block/sign-language/oled_text.json` | block | OK |  |
| `block/sign-language/result.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음<br>블록 `vision_load_tm` 정의 없음<br>블록 `vision_predict_tm` 정의 없음 |
| `block/sign-language/tts.json` | block | OK |  |
| `project/assistant-bot/main.py` | python | FAIL | L3: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L3: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_face import Face`<br>L3: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect`<br>L34: `Speech.tts()` 알 수 없는 키워드 인자 ['string']<br>L55: `Speech.tts()` 알 수 없는 키워드 인자 ['string']<br>L68: `Speech.tts()` 알 수 없는 키워드 인자 ['string']<br>L85: `Speech.tts()` 알 수 없는 키워드 인자 ['string']<br>L93: `Speech.tts()` 알 수 없는 키워드 인자 ['string']<br>… 외 1건 |
| `project/automove-bot/detect_marker.py` | python | FAIL | L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L3: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect` |
| `project/automove-bot/main.py` | python | FAIL | L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L3: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect`<br>L4: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_classify import TeachableMachine` |
| `project/face-recognition-bot/face_training.py` | python | FAIL | L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_face import Face`<br>L3: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera` |
| `project/face-recognition-bot/main.py` | python | FAIL | L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_face import Face`<br>L3: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera` |
| `project/face-recognition-simple/face_recognize.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_face import Face`<br>L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera` |
| `project/face-recognition-simple/face_train.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_face import Face`<br>L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera` |
| `project/face-tracking-bot/face_tracking.json` | block | FAIL | 블록 `vision_face` 정의 없음<br>블록 `vision_imshow_to_ide_img` 정의 없음 |
| `project/face-tracking-bot/main.py` | python | FAIL | L5: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L6: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_face import Face` |
| `project/guide-bot/main.py` | python | OK |  |
| `project/guide-bot/tts.py` | python | FAIL | L25: `Speech.tts()` 알 수 없는 키워드 인자 ['string'] |
| `project/pose-avatar/pose_avatar.json` | block | FAIL | 블록 `vision_analyze_pose` 입력 `val` 없음<br>블록 `vision_imshow_to_ide_img` 정의 없음 |
| `project/web-controller/main.py` | python | OK |  |
| `python/assistant/10_detect_all.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect`<br>L3: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_face import Face` |
| `python/assistant/11_detect_vis.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect`<br>L3: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_face import Face` |
| `python/assistant/12_detect_card.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect` |
| `python/assistant/13_conversation.py` | python | OK |  |
| `python/assistant/14_project.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect`<br>L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_face import Face`<br>L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L28: `Speech.tts()` 알 수 없는 키워드 인자 ['string']<br>L44: `Speech.tts()` 알 수 없는 키워드 인자 ['string']<br>L55: `Speech.tts()` 알 수 없는 키워드 인자 ['string']<br>L68: `Speech.tts()` 알 수 없는 키워드 인자 ['string']<br>L75: `Speech.tts()` 알 수 없는 키워드 인자 ['string']<br>… 외 1건 |
| `python/assistant/1_hello.py` | python | OK |  |
| `python/assistant/2_intro.py` | python | FAIL | L21: `Speech.tts()` 알 수 없는 키워드 인자 ['string'] |
| `python/assistant/3_clock.py` | python | FAIL | L20: `Speech.tts()` 알 수 없는 키워드 인자 ['string'] |
| `python/assistant/4_weather_collect.py` | python | OK |  |
| `python/assistant/5_news_collect.py` | python | OK |  |
| `python/assistant/6_motion_test.py` | python | OK |  |
| `python/assistant/7_weather_cast.py` | python | FAIL | L31: `Speech.tts()` 알 수 없는 키워드 인자 ['string'] |
| `python/assistant/8_news_cast.py` | python | FAIL | L30: `Speech.tts()` 알 수 없는 키워드 인자 ['string'] |
| `python/assistant/9_image_test.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera` |
| `python/assistant/timer_example.py` | python | FAIL | L13: `Speech.tts()` 알 수 없는 키워드 인자 ['string'] |
| `python/automove/1_hello.py` | python | OK |  |
| `python/automove/2_intro.py` | python | FAIL | L21: `Speech.tts()` 알 수 없는 키워드 인자 ['string'] |
| `python/automove/3_dance.py` | python | OK |  |
| `python/automove/4_image_test.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera` |
| `python/automove/5_predict_tm.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_classify import TeachableMachine`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera` |
| `python/automove/6_detect_marker.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect` |
| `python/automove/7_automove.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect` |
| `python/automove/8_automove_ext.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect` |
| `python/automove/9_automove_ext2.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect`<br>L3: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_classify import TeachableMachine` |
| `python/automove/timer_example.py` | python | FAIL | L13: `Speech.tts()` 알 수 없는 키워드 인자 ['string'] |
| `python/basics/b_function.py` | python | OK |  |
| `python/basics/b_list1.py` | python | OK |  |
| `python/basics/b_list2.py` | python | OK |  |
| `python/basics/b_logic1.py` | python | OK |  |
| `python/basics/b_logic2.py` | python | OK |  |
| `python/basics/b_logic3.py` | python | OK |  |
| `python/basics/b_loop1.py` | python | OK |  |
| `python/basics/b_loop2.py` | python | OK |  |
| `python/basics/b_math.py` | python | OK |  |
| `python/basics/b_text.py` | python | OK |  |
| `python/basics/b_variable.py` | python | OK |  |
| `python/basics/p_audio.py` | python | OK |  |
| `python/basics/p_collect.py` | python | OK |  |
| `python/basics/p_device.py` | python | OK |  |
| `python/basics/p_display.py` | python | OK |  |
| `python/basics/p_motion.py` | python | OK |  |
| `python/basics/p_vision1.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect`<br>L14: `Detect.classify_image()` 메서드 없음 |
| `python/basics/p_vision2.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect` |
| `python/basics/p_vision3.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_classify import TeachableMachine`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera` |
| `python/basics/p_voice.py` | python | FAIL | L17: `Speech.tts()` 알 수 없는 키워드 인자 ['string'] |
| `python/modules/audio/audio_test.py` | python | OK |  |
| `python/modules/collect/collect_test.py` | python | OK |  |
| `python/modules/device/device_once_test.py` | python | OK |  |
| `python/modules/device/device_test.py` | python | OK |  |
| `python/modules/device/device_test_with_thread.py` | python | OK |  |
| `python/modules/ext/gpio_test.py` | python | OK |  |
| `python/modules/ext/thread_test.py` | python | OK |  |
| `python/modules/ext/timer.py` | python | OK |  |
| `python/modules/ext/uart_test.py` | python | OK |  |
| `python/modules/motion/motion_test.py` | python | OK |  |
| `python/modules/motion/motor_test.py` | python | OK |  |
| `python/modules/motion/multi_motor_test.py` | python | OK |  |
| `python/modules/oled/figure_test.py` | python | OK |  |
| `python/modules/oled/image_test.py` | python | OK |  |
| `python/modules/oled/text_test.py` | python | OK |  |
| `python/modules/speech/.stt_local_test.py` | python | OK |  |
| `python/modules/speech/.tts_local_test.py` | python | OK |  |
| `python/modules/speech/chatbot_test.py` | python | FAIL | L53: `Dialog.mecab_morphs()` 메서드 없음 |
| `python/modules/speech/mecab_test.py` | python | FAIL | L10: `Dialog.mecab_pos()` 메서드 없음<br>L12: `Dialog.mecab_morphs()` 메서드 없음<br>L14: `Dialog.mecab_nouns()` 메서드 없음 |
| `python/modules/speech/stt_test.py` | python | OK |  |
| `python/modules/speech/tts_test.py` | python | OK |  |
| `python/modules/vision/camera_test.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera` |
| `python/modules/vision/detect_test.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_detect import Detect`<br>L3: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_face import Face` |
| `python/modules/vision/draw_test.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera` |
| `python/modules/vision/face_recognize.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_face import Face`<br>L19: `Face.get_ageGender()` 메서드 없음 |
| `python/modules/vision/face_train.py` | python | FAIL | L1: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_camera import Camera`<br>L2: 모듈 `openpibo.vision` 없음 → `from openpibo.vision_face import Face` |
