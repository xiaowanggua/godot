# Godot自定义构建配置 - 最小化体积版本（仅2D，无网络）
# Custom build configuration for minimal binary size (2D only, no networking)

# 生产环境优化
production = "yes"
deprecated = "no"
brotli = "no"

# 禁用3D功能（大幅减小体积）
disable_3d = "yes"

# 禁用XR（VR/AR）
disable_xr = "yes"

# 禁用3D物理
disable_physics_3d = "yes"

# 禁用3D导航
disable_navigation_3d = "yes"

# 保留高级GUI（包括RichTextLabel、GraphEdit等高级控件）
# disable_advanced_gui = "no"  # 默认已保留，无需设置

# 禁用的模块（包括网络相关）
module_bmp_enabled = "no"
module_enet_enabled = "no"           # 网络库 (Networking library)
module_gltf_enabled = "no"           # 3D模型格式 (3D model format)
module_gridmap_enabled = "no"        # 3D网格地图 (3D grid map)
module_hdr_enabled = "no"
module_jsonrpc_enabled = "no"        # 网络相关 (Networking related)
module_ktx_enabled = "no"
module_mbedtls_enabled = "no"        # TLS/SSL网络加密 (TLS/SSL encryption)
module_mobile_vr_enabled = "no"      # VR
module_multiplayer_enabled = "no"    # 多人联网 (Multiplayer networking)
module_navigation_enabled = "no"     # 导航（包括3D）(Navigation including 3D)
module_noise_enabled = "no"
module_ogg_enabled = "no"
module_openxr_enabled = "no"         # XR/VR
module_raycast_enabled = "no"        # 3D射线检测 (3D raycasting)
module_squish_enabled = "no"
module_svg_enabled = "no"
module_text_server_adv_enabled = "no"
module_tga_enabled = "no"
module_theora_enabled = "no"         # 视频编解码 (Video codec)
module_upnp_enabled = "no"           # 网络端口映射 (Network port mapping)
module_vorbis_enabled = "no"
module_webrtc_enabled = "no"         # 网络实时通信 (Real-time networking)
module_websocket_enabled = "no"      # WebSocket网络 (WebSocket networking)
module_webxr_enabled = "no"          # Web XR/VR
