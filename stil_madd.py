
from rich import print
import time
import argparse
from dronekit import connect, LocationGlobalRelative
from dronekit import VehicleMode as VMode
from dronekit import mavutil


def conn(connection_string=None):
    # # Set up option parsing to get connection string
    # parser = argparse.ArgumentParser(description='Commands V using V.simple_goto.')
    # parser.add_argument('--connect',
    #                     help="V connection target string. If not specified, SITL automatically started and used.")
    # args = parser.parse_args()

    # connection_string = args.connect
    # sitl = None


    # Start SITL if no connection string specified
    if connection_string == None:
        import dronekit_sitl
        sitl = dronekit_sitl.start_default()
        connection_string = sitl.connection_string()
        print(f'[yellow]Connecting to V on: [/yellow][blue]{connection_string}[/blue]')
        V = connect(connection_string, wait_ready=True)
        return V,sitl

    # Connect to the V
    print(f'[yellow]Connecting to V on: [/yellow][blue]{connection_string}[/blue]')
    V = connect(connection_string, wait_ready=True)
    return V
    

def Alt(V):
    return V.location.global_relative_frame.alt


def SAlt(V):
    return V.location.global_frame.alt


def rot(vehicle,heading=45,is_relative=1,wise=1):
    msg = vehicle.message_factory.command_long_encode(
    0, 0,    # target_system, target_component
    mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
    0, #confirmation
    heading,    # param 1, yaw in degrees
    0,          # param 2, yaw speed deg/s
    wise,          # param 3, direction -1 ccw, 1 cw
    is_relative, # param 4, relative offset 1, absolute angle 0
    
    0, 0, 0)    # param 5 ~ 7 not used
    
    # send command to vehicle
    vehicle.send_mavlink(msg)




def arm(V):
    """
    Arms V and fly to aTargetAltitude.
    """

    print("[yellow]Basic pre-arm checks[/yellow]")
    # Don't try to arm until autopilot is ready
    while not V.is_armable:
        print(" [yellow]Waiting for V to initialise...[/yellow]")
        time.sleep(1)

    print("[yellow]Arming motors[/yellow]")
    # Copter should arm in GUIDED mode
    V.mode = VMode("GUIDED")
    V.armed = True

    # Confirm V armed before attempting to take off
    while not V.armed:
        print(" [yellow]Waiting for arming...[/yellow]")
        time.sleep(1)

    print("[red]Taking off![/red]")


def Take_off(V,aTargetAltitude=1):
    V.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the V reaches a safe height before processing the goto
    #  (otherwise the command after V.simple_takeoff will execute
    #   immediately).
    while True:
        print(" Altitude: ", V.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if V.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

if __name__=="__main__":
    V=conn("127.0.0.1:14550")
    arm(V)
    Take_off(V,1)

    print("Set default/target airspeed to 3")
    V.airspeed = 3


    print ("Altitude (global frame): %s" % V.location.global_frame.alt)
    print ("Altitude (global relative frame): %s" % V.location.global_relative_frame.alt)
    print ("Altitude (NED frame): %s" % V.location.local_frame.down)


    # sleep so we can see the change in map
    
    rot(V,90)

    time.sleep(30)

    # print("Returning to Launch")
    # V.mode = VMode("RTL")
    
    print("Landing")
    V.mode = VMode("LAND")
    
    # Close V object before exiting script
    print("Close V object")
    V.close()

    # Shut down simulator if it was started.
