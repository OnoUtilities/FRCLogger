package org.usfirst.frc2337.libraries; //Change for your team

import edu.wpi.first.wpilibj.networktables.NetworkTable;
/***
 * ZLogger: a FRC based logging system that runs on the DriverStatiom 
 * @author Import-Python (OnoUtilities)
 *
 */
public class ZLogger {

	public String nt = "ZLogger"; //Main Table
	public NetworkTable table; //NT when starts
	public ZLogger() {
		table = NetworkTable.getTable(nt);
	}
	/***
	 * setEnabled()
	 * Enabled State of the Robot
	 */
	public void setEnabled() {
		table.putBoolean(nt + "/status", true);
	}
	/***
	 * setAutonEnabled()
	 * Enabled State of the Robot and make State to 'auton' 
	 */
	public void setAutonEnabled() {
		setEnabled();
		table.putString(nt + "/state", "auton");
	}
	/***
	 * setTelopEnabled()
	 * Enabled State of Robot and make State to 't' 
	 */
	public void setTelopEnabled() {
		setEnabled();
		table.putString(nt + "/state", "teleop");
	}
	/***
	 * setTelopEnabled()
	 * Disables the Robot  
	 */
	public void setDisabled() {
		table.putString(nt + "/state", "disabled");
	}
	public void sendDebug(String msg) {
		table.putString(nt + "/state", msg);
	}
	
}
