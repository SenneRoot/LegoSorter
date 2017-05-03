import com.hopding.jrpicam.RPiCamera;
import com.hopding.jrpicam.exceptions.FailedToRunRaspistillException;

import org.opencv.core.Mat;
import org.opencv.videoio.VideoCapture;

public class test
{
	static VideoCapture capture;
	static Mat webcam_image;
	
	public test()
	{
		 capture = new VideoCapture(0);
		 webcam_image = new Mat();
	}
	public static void main(String[] args)
	{
		capture.read(webcam_image);
	}
}