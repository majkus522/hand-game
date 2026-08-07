import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: window
    width: 350
    height: 200
    visible: true
    title: "PySide6 QML App"
    background: #129090

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 15

        Text {
            id: statusText
            text: backend.clickCount === 0 ? "Click the button to start!" : "Button clicked " + backend.clickCount + " time(s)!"
            font.pixelSize: 16
            Layout.alignment: Qt.AlignHCenter
        }

        Button {
            text: "Click Me"
            Layout.alignment: Qt.AlignHCenter
            onClicked: {
                backend.increment()
            }
        }
    }
}