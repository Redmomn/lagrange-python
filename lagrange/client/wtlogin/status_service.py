from lagrange.utils.binary.protobuf import proto_encode, proto_decode
from lagrange.info import AppInfo, DeviceInfo


# trpc.qq_new_tech.status_svc.StatusService.Register
def build_register_request(app: AppInfo, device: DeviceInfo) -> bytes:
    return proto_encode({
        1: device.guid,
        2: 0,
        3: app.current_version,
        4: 0,
        5: 2052,  # locale id
        6: {
            1: device.device_name,
            2: device.kernel_version,
            3: device.system_kernel,
            4: "",
            5: app.vendor_os
        },
        7: False,  # set_mute
        8: False,  # register_vendor_type
        9: True  # regtype
    })


# trpc.qq_new_tech.status_svc.StatusService.SsoHeartBeat
def build_sso_heartbeat_request() -> bytes:
    return proto_encode({1: 1})


def parse_register_response(response: bytes) -> bool:
    pb = proto_decode(response)
    if pb[2] == "register success":
        return True
    print(pb)
    return False