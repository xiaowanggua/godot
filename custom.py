# ==================================================================================
# Godot自定义构建配置 - 最小化体积版本（仅2D，无网络）
# Custom build configuration for minimal binary size (2D only, no networking)
# ==================================================================================

# ==================================================================================
# 基础生产环境优化配置
# ==================================================================================

# production = "yes"
# 说明：启用生产模式构建
# 效果：自动应用优化编译选项，包括LTO（链接时优化）、更高的优化级别等
# 禁用的功能：开发模式的调试辅助功能、详细日志输出
production = "yes"

# deprecated = "no"
# 说明：禁用已弃用的API和功能
# 效果：移除旧版本的兼容代码，减小二进制体积
# 禁用的功能：Godot 3.x及更早版本的兼容API、已标记为弃用的类和方法
deprecated = "no"

# brotli = "no"
# 说明：禁用Brotli压缩支持
# 效果：移除Brotli压缩/解压缩功能
# 禁用的功能：资源的Brotli压缩、WOFF2字体支持（需要Brotli）
brotli = "no"

# ==================================================================================
# 禁用3D相关功能（大幅减小体积）
# ==================================================================================

# disable_3d = "yes"
# 说明：完全禁用3D渲染引擎
# 效果：移除整个3D渲染管线、3D节点、3D资源处理
# 禁用的功能：
#   - 所有3D节点（Node3D、MeshInstance3D、Camera3D等）
#   - 3D场景渲染
#   - 3D材质和着色器
#   - 3D光照和阴影
#   - 3D粒子系统
#   - 骨骼动画（3D）
disable_3d = "yes"

# disable_xr = "yes"
# 说明：禁用XR（扩展现实）功能
# 效果：移除VR/AR相关的API和功能
# 禁用的功能：
#   - XRInterface（VR/AR接口）
#   - XRServer（XR服务器）
#   - XRCamera3D、XRController3D等节点
#   - OpenXR、WebXR等XR平台支持
disable_xr = "yes"

# disable_physics_3d = "yes"
# 说明：禁用3D物理引擎
# 效果：移除3D物理模拟功能
# 禁用的功能：
#   - PhysicsServer3D（3D物理服务器）
#   - RigidBody3D、StaticBody3D、CharacterBody3D等3D物理节点
#   - CollisionShape3D、Area3D等3D碰撞检测
#   - 3D射线检测
#   - 3D物理材质
disable_physics_3d = "yes"

# disable_navigation_3d = "yes"
# 说明：禁用3D导航系统
# 效果：移除3D寻路和导航网格功能
# 禁用的功能：
#   - NavigationServer3D（3D导航服务器）
#   - NavigationRegion3D、NavigationAgent3D等3D导航节点
#   - 3D导航网格烘焙
#   - 3D路径规划
disable_navigation_3d = "yes"

# ==================================================================================
# 保留的GUI和字体功能（重要！）
# ==================================================================================

# disable_advanced_gui = "no"
# 说明：显式保留高级GUI功能（修复SpinBox、Button、Container等控件显示问题）
# 保留的功能：
#   - SpinBox（数字输入框）
#   - Button及其变体（Button、CheckButton、LinkButton等）
#   - Container及其子类（VBoxContainer、HBoxContainer、GridContainer等）
#   - RichTextLabel（富文本标签，支持BBCode）
#   - GraphEdit、GraphNode（图形编辑器节点）
#   - Tree（树形控件）
#   - ItemList（项目列表）
#   - TabContainer、TabBar（标签页容器）
#   - SplitContainer（分割容器）
#   - 等所有高级GUI控件和行为
disable_advanced_gui = "no"

# ==================================================================================
# 禁用的可选模块
# ==================================================================================

# module_bmp_enabled = "no"
# 说明：禁用BMP图像格式支持
# 禁用的功能：导入和使用.bmp图片文件
module_bmp_enabled = "no"

# module_enet_enabled = "no"
# 说明：禁用ENet网络库
# 禁用的功能：
#   - 高性能UDP网络传输
#   - ENetConnection、ENetPacketPeer等网络类
#   - 基于ENet的多人游戏网络功能
module_enet_enabled = "no"

# module_gltf_enabled = "no"
# 说明：禁用glTF 3D模型格式支持
# 禁用的功能：
#   - 导入.gltf和.glb 3D模型文件
#   - glTF场景导入器
#   - GLTFDocument、GLTFState等类
module_gltf_enabled = "no"

# module_gridmap_enabled = "no"
# 说明：禁用GridMap（3D网格地图）
# 禁用的功能：
#   - GridMap节点（用于创建基于网格的3D关卡）
#   - MeshLibrary（网格库资源）
#   - 3D体素风格的关卡编辑
module_gridmap_enabled = "no"

# module_hdr_enabled = "no"
# 说明：禁用HDR图像格式支持
# 禁用的功能：
#   - Radiance HDR (.hdr)图像格式导入
#   - 用于环境贴图和天空盒的HDR纹理
module_hdr_enabled = "no"

# module_jsonrpc_enabled = "no"
# 说明：禁用JSON-RPC协议支持
# 禁用的功能：
#   - JSONRPC类（远程过程调用）
#   - 基于JSON的RPC通信
#   - 用于编辑器插件和LSP（语言服务器协议）的RPC功能
module_jsonrpc_enabled = "no"

# module_ktx_enabled = "no"
# 说明：禁用KTX纹理格式支持
# 禁用的功能：
#   - Khronos Texture (.ktx)格式导入
#   - GPU压缩纹理格式（如ETC2、ASTC等）的容器格式
module_ktx_enabled = "no"

# module_mbedtls_enabled = "no"
# 说明：禁用mbedTLS加密库
# 禁用的功能：
#   - TLS/SSL加密连接
#   - HTTPS请求
#   - 加密的网络通信
#   - Crypto、HashingContext、TLSOptions等加密相关类
#   - 安全的WebSocket连接
module_mbedtls_enabled = "no"

# module_mobile_vr_enabled = "no"
# 说明：禁用移动VR支持
# 禁用的功能：
#   - 移动平台的VR功能（如Google Cardboard）
#   - MobileVRInterface
module_mobile_vr_enabled = "no"

# module_multiplayer_enabled = "no"
# 说明：禁用多人游戏（Multiplayer）模块
# 禁用的功能：
#   - MultiplayerAPI、MultiplayerPeer等多人游戏核心类
#   - 高级多人游戏同步功能
#   - MultiplayerSpawner、MultiplayerSynchronizer节点
#   - RPC（远程过程调用）功能
#   - 场景复制和状态同步
module_multiplayer_enabled = "no"

# module_navigation_enabled = "no"
# 说明：禁用导航（Navigation）模块
# 禁用的功能：
#   - 2D和3D导航系统的共享功能
#   - NavigationServer基础类
#   - A*寻路算法
#   - 导航网格数据结构
module_navigation_enabled = "no"

# module_noise_enabled = "no"
# 说明：禁用噪声生成模块
# 禁用的功能：
#   - Noise、FastNoiseLite等噪声生成类
#   - 程序化噪声纹理生成
#   - 用于地形生成、程序化内容的噪声算法
module_noise_enabled = "no"

# module_ogg_enabled = "no"
# 说明：禁用OGG容器格式支持
# 禁用的功能：
#   - .ogg音频文件格式支持
#   - 与Vorbis/Opus音频编解码器的OGG封装
module_ogg_enabled = "no"

# module_openxr_enabled = "no"
# 说明：禁用OpenXR（开放式XR标准）支持
# 禁用的功能：
#   - OpenXR API集成
#   - 跨平台VR/AR设备支持
#   - Meta Quest、HTC Vive、Windows Mixed Reality等设备支持
module_openxr_enabled = "no"

# module_raycast_enabled = "no"
# 说明：禁用Embree光线追踪库
# 禁用的功能：
#   - 基于Embree的高性能光线投射
#   - 光照贴图烘焙的优化
#   - 精确的3D射线检测
module_raycast_enabled = "no"

# module_squish_enabled = "no"
# 说明：禁用Squish纹理压缩库
# 禁用的功能：
#   - DXT/BC纹理压缩
#   - 高质量的纹理压缩算法
module_squish_enabled = "no"

# module_svg_enabled = "no"
# 说明：禁用SVG矢量图形支持
# 禁用的功能：
#   - SVG文件导入和渲染
#   - 矢量图形显示
#   - 编辑器图标的SVG格式（会降级到PNG）
module_svg_enabled = "no"

# module_text_server_adv_enabled = "yes"
# 说明：启用高级文本服务器（TextServerAdvanced）- 支持自定义字体！
# 效果：提供完整的字体渲染和排版支持
# 保留的功能：
#   - 自定义字体文件加载和渲染（TTF、OTF等）
#   - 复杂脚本支持（阿拉伯语、希伯来语等从右到左的文字）
#   - 高级排版功能（字距调整、连字等）
#   - OpenType特性支持
#   - 多语言字体支持
#   - 字体回退机制
# 注意：禁用此模块会导致自定义字体无法正常显示！
module_text_server_adv_enabled = "yes"

# module_tga_enabled = "no"
# 说明：禁用TGA图像格式支持
# 禁用的功能：
#   - Targa (.tga)图像文件导入
module_tga_enabled = "no"

# module_theora_enabled = "no"
# 说明：禁用Theora视频编解码器
# 禁用的功能：
#   - .ogv视频文件播放
#   - Theora视频解码
#   - VideoStreamTheora
module_theora_enabled = "no"

# module_upnp_enabled = "no"
# 说明：禁用UPnP（通用即插即用）网络支持
# 禁用的功能：
#   - UPNP、UPNPDevice类
#   - 自动端口映射（NAT穿透）
#   - 局域网设备发现
module_upnp_enabled = "no"

# module_vorbis_enabled = "no"
# 说明：禁用Vorbis音频编解码器
# 禁用的功能：
#   - .ogg音频文件播放（Vorbis编码）
#   - AudioStreamOggVorbis
#   - 高质量的音频压缩
module_vorbis_enabled = "no"

# module_webrtc_enabled = "no"
# 说明：禁用WebRTC（实时通信）支持
# 禁用的功能：
#   - WebRTC网络协议
#   - WebRTCPeerConnection、WebRTCDataChannel等类
#   - 点对点音视频通信
#   - 低延迟的实时数据传输
module_webrtc_enabled = "no"

# module_websocket_enabled = "no"
# 说明：禁用WebSocket协议支持
# 禁用的功能：
#   - WebSocketClient、WebSocketServer类
#   - WebSocket网络连接
#   - 全双工实时通信
#   - 常用于HTML5导出和实时网络游戏
module_websocket_enabled = "no"

# module_webxr_enabled = "no"
# 说明：禁用WebXR（Web扩展现实）支持
# 禁用的功能：
#   - 浏览器中的VR/AR支持
#   - WebXRInterface
#   - HTML5平台的XR功能
module_webxr_enabled = "no"

# ==================================================================================
# 配置总结
# ==================================================================================
# 
# ✅ 保留的主要功能：
# - 完整的2D游戏引擎（节点、场景、渲染）
# - 2D物理引擎（PhysicsServer2D、RigidBody2D等）
# - 2D导航系统（但navigation模块被禁用，只保留基础功能）
# - GDScript脚本语言
# - 完整的GUI系统（包括高级GUI控件：SpinBox、Button、Container等）✅
# - 高级文本服务器（支持自定义字体、TTF/OTF文件）✅
# - 字体渲染模块（FreeType、MSDFGEN）✅
# - 音频系统（基础音频，但无Vorbis/Ogg支持）
# - 输入处理系统
# - 动画系统（AnimationPlayer、Tween等）
# - 资源管理系统
# - 基础图像格式（PNG、JPG等）
# 
# ❌ 禁用的主要功能：
# - 所有3D相关功能（渲染、物理、导航）
# - 所有网络功能（ENet、WebSocket、WebRTC、多人游戏）
# - 所有XR/VR/AR功能
# - 视频播放
# - 某些图像和音频格式（BMP、TGA、HDR、Ogg/Vorbis）
# - SVG矢量图形
# - 加密和HTTPS
# 
# 🎯 适用场景：
# - 纯2D游戏（无3D需求）
# - 单机游戏（无联网需求）
# - 需要自定义字体的游戏 ✅
# - 需要完整GUI控件的应用 ✅
# - 不需要VR/AR的项目
# - 追求合理体积的项目（相比完整版本仍然大幅减小）
# 
# 📊 预期体积变化：
# - 相比之前版本会稍大（增加text_server_adv支持）
# - 但仍比完整版本小很多（禁用了3D和网络）
# - 预计约40-45MB（之前是36MB）
# 
# ==================================================================================
