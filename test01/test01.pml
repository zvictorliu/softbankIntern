<?xml version="1.0" encoding="UTF-8" ?>
<Package name="test01" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="main" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="move" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="zimu" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="dialog1" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="dialog2" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="dialog3" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="pepper1" src="html/pepper1.mp4" />
        <File name="pepper2" src="html/pepper2.mp4" />
        <File name="pepper3" src="html/pepper3.mp4" />
        <File name="ask" src="html/ask1.mp4" />
        <File name="ask2" src="html/ask2.mp4" />
        <File name="ask3" src="html/ask3.mp4" />
        <File name="pic" src="html/pic.png" />
    </Resources>
    <Topics />
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
        <Translation name="translation_zh_CN" src="translations/translation_zh_CN.ts" language="zh_CN" />
    </Translations>
</Package>
