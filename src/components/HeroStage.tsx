import { motion, useReducedMotion } from "motion/react";
import { lazy, Suspense, useEffect, useState } from "react";

const ParticleCanvas = lazy(() => import("./ParticleCanvas"));

export default function HeroStage() {
  const reduced = useReducedMotion() ?? false;
  const [webgl, setWebgl] = useState(false);

  useEffect(() => {
    try {
      const canvas = document.createElement("canvas");
      const supported = Boolean(canvas.getContext("webgl2") || canvas.getContext("webgl"));
      setWebgl(supported);
    } catch {
      setWebgl(false);
    }
  }, []);

  return (
    <div className="hero-stage" aria-hidden="true">
      <div className="hero-stage__fallback">
        <span className="hero-orbit hero-orbit--one" />
        <span className="hero-orbit hero-orbit--two" />
        <span className="hero-orbit hero-orbit--three" />
        <span className="hero-core" />
      </div>
      {webgl && (
        <div className="hero-stage__canvas">
          <Suspense fallback={null}>
            <ParticleCanvas reduced={reduced} />
          </Suspense>
        </div>
      )}
      <motion.span className="hero-chip hero-chip--one" initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.45, duration: 0.7 }}>
        DESIGN
      </motion.span>
      <motion.span className="hero-chip hero-chip--two" initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.7, duration: 0.7 }}>
        BUILD
      </motion.span>
      <motion.span className="hero-chip hero-chip--three" initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.95, duration: 0.7 }}>
        WRITE
      </motion.span>
    </div>
  );
}
