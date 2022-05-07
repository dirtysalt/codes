package com.dirlt.java.jni;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;

public class RunNativeLibrary {
    public static native void hello();

    public static void LoadLibraryInJAR(Class cls, String pathInJAR, int bufferSize, boolean deleteOnSuccess)
            throws UnsatisfiedLinkError {
        try {
            InputStream is = cls.getResourceAsStream(pathInJAR);
            File f = File.createTempFile(cls.getCanonicalName() + ".jni-", ".so");
            FileOutputStream fos = new FileOutputStream(f);
            byte[] buffer = new byte[bufferSize];
            while (true) {
                int size = is.read(buffer);
                fos.write(buffer, 0, size);
                if (size < bufferSize) {
                    break;
                }
            }
            is.close();
            fos.close();
            System.load(f.getPath());
            if (deleteOnSuccess) {
                f.delete();
            }
        } catch (IOException e) {
            UnsatisfiedLinkError ex = new UnsatisfiedLinkError();
            ex.initCause(e);
            throw ex;
        }
    }

    public static void LoadLibraryInJAR(Class cls, String pathInJAR) throws UnsatisfiedLinkError {
        LoadLibraryInJAR(cls, pathInJAR, 64 * 1024, true);
    }

    static {
        LoadLibraryInJAR(RunNativeLibrary.class, "/libnative.so");
    }

    public static void main(String[] args) {
        hello();
    }
}
